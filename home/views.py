"""
Views defined for the 'home' app
"""
from django.shortcuts import render, get_object_or_404
from products.models import Game, Publisher


def index(request):
    """
    A view to return the index page and spme featured games
    """
    sm64 = get_object_or_404(Game, name='Super Mario 64')
    crash = get_object_or_404(Game, name='Crash Bandicoot 3')
    sonic = get_object_or_404(Game, name='Sonic the Hedgehog')
    pac_man = get_object_or_404(Game, name='Pac-Man')
    publishers = Publisher.objects.all()

    context = {
        'sm64': sm64,
        'crash': crash,
        'sonic': sonic,
        'pac_man': pac_man,
        'publishers': publishers,
    }
    return render(request, 'home/index.html', context)
