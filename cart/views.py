"""
Views defined for the 'cart' app
"""
from django.shortcuts import (render, redirect, reverse, HttpResponse,
                              get_object_or_404)
from django.contrib import messages

from listings.models import Listing


def view_cart(request):
    """
    A view that renders the cart contents page
    """

    return render(request, 'cart/cart.html', context={'show_cart': True})


def add_to_cart(request, product_id):
    """
    A view that adds items to the cart
    """

    listing = get_object_or_404(Listing, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        if cart[product_id] + quantity > listing.copies_available:
            messages.error(request, "Sorry, the storefront doesn't have that \
                many copies available.")
        else:
            cart[product_id] += quantity
            messages.success(request,
                             f'Updated {listing.title} quantity in your cart')
    else:
        cart[product_id] = quantity
        messages.success(request, f'Added {listing.title} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """
    A view that adjusts the quantity of items in the cart
    """
    listing = get_object_or_404(Listing, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        if quantity > listing.copies_available:
            messages.error(request, "Sorry, the storefront doesn't have that \
                many copies available.")
        else:
            cart[product_id] = quantity
            messages.success(request,
                             f'Updated {listing.title} quantity in your cart')
    else:
        cart.pop(product_id)
        messages.success(request, f'Removed {listing.title} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):
    """
    A view that removes items from the cart
    """
    cart = request.session.get('cart', {})
    try:
        listing = get_object_or_404(Listing, pk=product_id)
        cart.pop(product_id)
        messages.success(request, f'Removed {listing.title} from your cart')
        request.session['cart'] = cart

        return redirect(reverse('view_cart'))

    except Exception as e:  # noqa: F841
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
