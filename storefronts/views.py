"""
Views for the profiles app.
"""
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .models import StoreFront
from .forms import StoreFrontForm


@login_required
def storefront_preamble(request):
    """
    A preamble to the storfront app, for users that haven't yet created one.
    """

    template = 'storefronts/preamble.html'
    return render(request, template)


@login_required
def add_storefront(request):
    """
    A view for users to create a storefront on the site.
    """

    if request.method == 'POST':
        form = StoreFrontForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Congratulations, you've successfully started a \
                    storefront!")
    else:
        form = StoreFrontForm()

    template = 'storefronts/add_storefront.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
