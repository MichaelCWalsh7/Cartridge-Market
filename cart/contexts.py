"""
Context processor for the cart items
"""
from django.shortcuts import get_object_or_404
from listings.models import Listing


def cart_contents(request):
    """
    Returns the context dictionary for use in various templates.
    """
    # pylint: disable=unused-argument
    cart_items = []
    total = 0
    grand_total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        listing = get_object_or_404(Listing, pk=item_id)
        total = quantity * listing.price
        grand_total += total
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'listing': listing,
            'total': total,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
