"""
Views defined for the 'checkout' app
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    A view to show the checkout form to the user.
    """
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('all_games'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': ('pk_test_51Jo841KhzigfW6e3RYsQhgqugeGxqruSFcU4hx'
                              'DCkMhpWM4F5tNNOu7P0EcNIQitRXp0jfqKe106LFMK6KI6'
                              '3IEL00tNyAzgK6'),
    }

    return render(request, template, context)
