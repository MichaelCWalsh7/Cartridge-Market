"""
Views difined for the 'home' app
"""
# pylint: disable=no-member
from django.shortcuts import render
from products.models import Game


def all_games(request):
    """
    A view to show all games currently available on the site.
    """
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'products/all_games.html', context)
