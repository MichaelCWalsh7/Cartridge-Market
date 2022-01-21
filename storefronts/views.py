"""
Views for the profiles app.
"""
from django.shortcuts import render


def storefront_preamble(request):
    """
    A preamble to the storfront app, for users that haven't yet created one.
    """

    template = 'storefronts/preamble.html'
    return render(request, template)
