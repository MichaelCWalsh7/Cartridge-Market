"""
Views defined for the 'checkout' app
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

import stripe

from cart.contexts import cart_contents
from .forms import OrderForm


def checkout(request):
    """
    A view to show the checkout form to the user.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('all_games'))

    current_cart = cart_contents(request)
    current_cart_total = current_cart['grand_total']
    stripe_total = round(current_cart_total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }

    return render(request, template, context)
