"""
Views for the profiles app.
"""
# pylint: disable=redefined-outer-name
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

    template = 'storefronts/storefront.html'
    context = {
        'storefront': storefront,
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


def edit_storefront(request, storefront_id):
    """
    A view for users to edit their storefront on the site.
    """
    storefront = get_object_or_404(StoreFront, pk=storefront_id)
    if request.method == 'POST':
        form = StoreFrontForm(request.POST, request.FILES, instance=storefront)
        if form.is_valid():
            image_url = request.POST.get('image_url')
            storefront = form.save(commit=False)
            storefront.image_url = image_url
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
