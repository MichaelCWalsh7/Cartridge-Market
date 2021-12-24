"""
Context processor for the cart items
"""


def cart_contents(request):
    """
    Returns the context dictionary for use in various templates.
    """
    # pylint: disable=unused-argument
    cart_items = []
    total = 0
    product_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
    }

    return context
