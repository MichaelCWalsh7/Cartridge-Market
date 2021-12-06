"""
Views difined for the 'home' app
"""
# pylint: disable=no-member
from django.shortcuts import render
from products.models import Game, Brand


def index(request):
    """
    A view to return the index page and spme featured games
    """
    sm64 = Game.objects.all().filter(sku='FG-1')
    crash = Game.objects.all().filter(sku='FG-2')
    sonic = Game.objects.all().filter(sku='FG-3')
    pac_man = Game.objects.all().filter(sku='FG-4')
    brands = Brand.objects.all()

    context = {
        'sm64': sm64,
        'crash': crash,
        'sonic': sonic,
        'pac_man': pac_man,
        'brands': brands,
    }
    return render(request, 'home/index.html', context)
