"""
Views for the profiles app.
"""
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order
from storefronts.models import StoreFront

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    A view to display the user's profile.
    """
    # pylint: disable=redefined-outer-name
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    storefront = get_object_or_404(StoreFront, user=request.user)

    template = 'profiles/profile.html'
    if storefront:
        context = {
            'form': form,
            'orders': orders,
            'storefront': storefront,
            'on_profile_page': True,
        }
    else:
        context = {
            'form': form,
            'orders': orders,
        }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    A view to display the users order history.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request, f'This is a past confirmation for order number {order_number}'
        'A confirmation email was sent on the order date.'
    )

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
