"""
Views defined for the 'products' app
"""
# pylint: disable=no-member
from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.db.models import Q

from products.models import Game


def all_games(request):
    """
    A view to show all games currently available on the site.
    """
    games = Game.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_games'))

            queries = Q(
                name__icontains=query
            ) | Q(
                    description__icontains=query
            ) | Q(
                    genre__name__icontains=query
            ) | Q(
                    publisher__name__icontains=query
            ) | Q(
                    console__name__icontains=query
            )
            games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'products/all_games.html', context)


def nintendo_games(request):
    """
    A view to show all Nintendo games currently available on the site.
    """
    games = Game.objects.filter(publisher__name="Nintendo")
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_games'))

            queries = Q(
                name__icontains=query
            ) | Q(
                    description__icontains=query
            ) | Q(
                    genre__name__icontains=query
            ) | Q(
                    publisher__name__icontains=query
            ) | Q(
                    console__name__icontains=query
            )
            games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'products/nintendo_games.html', context)


def sega_games(request):
    """
    A view to show all Sega games currently available on the site.
    """
    games = Game.objects.filter(publisher__name="Sega")
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_games'))

            queries = Q(
                name__icontains=query
            ) | Q(
                    description__icontains=query
            ) | Q(
                    genre__name__icontains=query
            ) | Q(
                    publisher__name__icontains=query
            ) | Q(
                    console__name__icontains=query
            )
            games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'products/sega_games.html', context)


def sony_games(request):
    """
    A view to show all Sony games currently available on the site.
    """
    games = Game.objects.filter(publisher__name="Sony")
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_games'))

            queries = Q(
                name__icontains=query
            ) | Q(
                    description__icontains=query
            ) | Q(
                    genre__name__icontains=query
            ) | Q(
                    publisher__name__icontains=query
            ) | Q(
                    console__name__icontains=query
            )
            games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'products/sony_games.html', context)


def atari_games(request):
    """
    A view to show all Atari games currently available on the site.
    """
    games = Game.objects.filter(publisher__name="Atari")
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_games'))

            queries = Q(
                name__icontains=query
            ) | Q(
                    description__icontains=query
            ) | Q(
                    genre__name__icontains=query
            ) | Q(
                    publisher__name__icontains=query
            ) | Q(
                    console__name__icontains=query
            )
            games = games.filter(queries)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'products/atari_games.html', context)
