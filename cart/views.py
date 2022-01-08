"""
Views defined for the 'cart' app
"""
# pylint: disable=unused-variable,broad-except,invalid-name
from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):
    """
    A view that renders the cart contents page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """
    A view that adds items to the cart
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, product_id):
    """
    A view that adjusts the quantity of items in the cart
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[product_id] = quantity
    else:
        cart.pop(product_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, product_id):
    """
    A view that removes items from the cart
    """
    cart = request.session.get('cart', {})
    try:
        cart.pop(product_id)
        request.session['cart'] = cart

        return redirect(reverse('view_cart'))

    except Exception as e:  # noqa: F841
        return HttpResponse(status=500)
