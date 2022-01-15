"""
Views defined for the 'checkout' app
"""
# pylint: disable=no-member
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

import stripe

from cart.contexts import cart_contents
from products.models import Game
from .forms import Order, OrderForm
from .models import OrderLineItem


def checkout(request):
    """
    A view to show the checkout form to the user.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in cart.items():
                try:
                    game = Game.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            game=game,
                            quantity=item_data,
                        )
                        order_line_item.save()

                except Game.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your cart wasn't found in our"
                        "database. Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request,
                           'There was an error with your order form.'
                           'Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request,
                           "There's nothing in your cart at the moment")
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


def checkout_success(request, order_number):
    """
    A view to handle when the checkout has been successful.
    """
    # pylint: disable=unused-variable
    save_info = request.session.get('save_info')  # noqa: F841
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation email will be \
        sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)