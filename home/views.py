"""
Views difined for the 'home' app
"""
# pylint: disable=no-member
from django.shortcuts import render
from products.models import Game, Publisher


def index(request):
    """
    A view to return the index page and spme featured games
    """
    sm64 = Game.objects.all().filter(sku='FG-1')
    crash = Game.objects.all().filter(sku='FG-2')
    sonic = Game.objects.all().filter(sku='FG-3')
    pac_man = Game.objects.all().filter(sku='FG-4')
    publishers = Publisher.objects.all()

    context = {
        'sm64': sm64,
        'crash': crash,
        'sonic': sonic,
        'pac_man': pac_man,
        'publishers': publishers,
    }
    return render(request, 'home/index.html', context)
