"""
Context processor for the cart items
"""
from django.shortcuts import get_object_or_404
from products.models import Game


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
        game = get_object_or_404(Game, pk=item_id)
        total = quantity * game.price
        grand_total += total
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'game': game,
            'total': total,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
