"""
Views for the profiles app.
"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from listings.models import Listing
from .models import StoreFront
from .forms import StoreFrontForm


@login_required
def storefront_preamble(request):
    """
    A preamble to the storfront app, for users that haven't yet created one.
    """
    template = 'storefronts/preamble.html'
    return render(request, template)


def storefront(request, storefront_id):
    """
    A view to show an individual storefront.
    """
    storefront = get_object_or_404(StoreFront, pk=storefront_id)

    all_listings = Listing.objects.all()
    listings = all_listings.filter(storefront=storefront_id)

    template = 'storefronts/storefront.html'
    context = {
        'storefront': storefront,
        'listings': listings,
    }
    return render(request, template, context)


@login_required
def add_storefront(request):
    """
    A view for users to create a storefront on the site.
    """

    if request.method == 'POST':
        form = StoreFrontForm(request.POST, request.FILES)
        if form.is_valid():
            image_url = request.POST.get('image_url')
            storefront = form.save(commit=False)
            storefront.image_url = image_url
            storefront.user = request.user
            storefront.save()
            messages.success(
                request, "Congratulations, you've successfully started a \
                    storefront!")
            return redirect(reverse('storefront', args=[storefront.id]))
        else:
            messages.error(request, 'Failed to add storefront. Please ensure \
                your form is valid.')
    else:
        form = StoreFrontForm()

    template = 'storefronts/add_storefront.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_storefront(request, storefront_id):
    """
    A view for users to edit their storefront on the site.
    """
    storefront = get_object_or_404(StoreFront, pk=storefront_id)
    if storefront.user != request.user:
        messages.warning(request, "Sorry, only a storefront owner may edit a \
            storefront.")
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = StoreFrontForm(request.POST, request.FILES, instance=storefront)
        if form.is_valid():
            image_url_field = request.POST.get('image_url')
            if image_url_field is None:
                image_url = storefront.image_url
            else:
                image_url = image_url_field
            storefront.image_url = image_url
            storefront = form.save(commit=False)
            storefront.user = request.user
            storefront.save()
            messages.success(request, "Successfully updated storefront.")
            return redirect(reverse('storefront', args=[storefront.id]))
        else:
            messages.error(request, 'Failed to update storefront. Please \
                ensure your form is valid.')

    form = StoreFrontForm(instance=storefront)
    messages.info(
        request, f'You are editing your storefront, {storefront.name}')

    template = 'storefronts/edit_storefront.html'
    context = {
        'form': form,
        'storefront': storefront,
    }

    return render(request, template, context)


@login_required
def delete_storefront(request, storefront_id):
    """
    A view for users to delete their storefront on the site.
    """
    storefront = get_object_or_404(StoreFront, pk=storefront_id)
    if storefront.user != request.user:
        messages.warning(request, "Sorry, only a storefront owner may delete \
            a storefront.")
        return redirect(reverse('home'))
    storefront.delete()
    messages.success(request, 'Your storefront has been deleted.')
    return redirect(reverse('home'))


def all_storefronts(request):
    """
    A view to display all storefronts currently uploaded on the site.
    """
    storefronts = StoreFront.objects.all()
    query = None

    if request.GET:
        # Handles searches made on the site
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_storefronts'))

            # queries are applied to name, description, console and publisher
            queries = Q(
                name__icontains=query
            ) | Q(
                    description__icontains=query
            )
            storefronts = storefronts.filter(queries)

    context = {
        'storefronts': storefronts,
        'search_term': query,
    }

    return render(request, 'storefronts/all_storefronts.html', context)
