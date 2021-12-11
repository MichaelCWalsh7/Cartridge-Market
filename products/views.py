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

        if 'filter_publisher' in request.GET:
            publisher = request.GET['filter_publisher']
            if publisher != "any":
                games = games.filter(publisher__name=publisher)
        if 'console' in request.GET:
            console = request.GET['console']
            if console != "any":
                games = games.filter(console__name=console)
        if 'genre' in request.GET:
            genre = request.GET['genre']
            if genre != "any":
                games = games.filter(genre__name=genre)

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'products/all_games.html', context)


def publisher_games(request, publisher):
    """
    A view to show all Nintendo games currently available on the site.
    """
    games = Game.objects.filter(publisher__name=publisher)
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

    lpublisher = publisher.lower()

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, f'products/{lpublisher}_games.html', context)
