"""
Views for the listings app.
"""
# pylint: disable=no-member
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from products.models import Game
from .forms import ListingtForm


@login_required
def add_listing(request):
    """
    A view for users to create a listing on the site.
    """
    games = Game.objects.all()
    nintendo_games = games.filter(publisher__name='Nintendo')
    sony_games = games.filter(publisher__name='Sony')
    sega_games = games.filter(publisher__name='Sega')
    atari_games = games.filter(publisher__name='Atari')

    form = ListingtForm(request.POST, request.FILES)

    template = 'listings/add_listing.html'
    context = {
        'games': games,
        'nintendo_games': nintendo_games,
        'sony_games': sony_games,
        'sega_games': sega_games,
        'atari_games': atari_games,
        'form': form,
    }
    return render(request, template, context)
