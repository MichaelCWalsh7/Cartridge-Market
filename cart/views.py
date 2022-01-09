"""
Views defined for the 'cart' app
"""
# pylint: disable=broad-except,invalid-name
from django.shortcuts import (render, redirect, reverse, HttpResponse,
                              get_object_or_404)
from django.contrib import messages

from products.models import Game


def view_cart(request):
    """
    A view that renders the cart contents page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """
    A view that adds items to the cart
    """

    game = get_object_or_404(Game, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
        messages.success(request,
                         f'Updated {game.name} quantity in your cart')
    else:
        cart[product_id] = quantity
        messages.success(request, f'Added {game.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """
    A view that adjusts the quantity of items in the cart
    """
    game = get_object_or_404(Game, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
        messages.success(request,
                         f'Updated {game.name} quantity in your cart')
    else:
        cart.pop(product_id)
        messages.success(request, f'Removed {game.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):
    """
    A view that removes items from the cart
    """
    cart = request.session.get('cart', {})
    try:
        game = get_object_or_404(Game, pk=product_id)
        cart.pop(product_id)
        messages.success(request, f'Removed {game.name} from your cart')
        request.session['cart'] = cart

        return redirect(reverse('view_cart'))

    except Exception as e:  # noqa: F841
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
