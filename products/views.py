"""
Views defined for the 'products' app
"""
# pylint: disable=no-member
from django.shortcuts import render, reverse, redirect, get_object_or_404
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
        # Handles searches made on the site
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('all_games'))

            # queries are applied to name, description, console and publisher
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

        # logic to filter games by publisher, genre or console
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

        # logic to handle sorting from the site's filter container
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort != "default":
                sortkeys = sort.split('-')
                direction_string = sortkeys[1]
                if direction_string == 'asc':
                    direction = ''
                elif direction_string == 'dsc':
                    direction = '-'
            if sortkeys:
                category = sortkeys[0]
                games = games.order_by(f'{direction}{category}')

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, 'products/all_games.html', context)


def publisher_games(request, publisher):
    """
    A view to show all games currently available on the site, ordered and
    styled by publihser.
    """
    games = Game.objects.filter(publisher__name=publisher)
    query = None

    if request.GET:
        if 'q' in request.GET:
            # Handles searches made on the site
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

        # logic to filter games by publisher, genre or console
        if 'filter_publisher' in request.GET:
            filter_publisher = request.GET['filter_publisher']
            if filter_publisher != "any":
                games = games.filter(publisher__name=filter_publisher)
        if 'console' in request.GET:
            console = request.GET['console']
            if console != "any":
                games = games.filter(console__name=console)
        if 'genre' in request.GET:
            genre = request.GET['genre']
            if genre != "any":
                games = games.filter(genre__name=genre)

        # logic to handle sorting from the site's filter container
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort != "default":
                sortkeys = sort.split('-')
                direction_string = sortkeys[1]
                if direction_string == 'asc':
                    direction = ''
                elif direction_string == 'dsc':
                    direction = '-'

            category = sortkeys[0]
            games = games.order_by(f'{direction}{category}')

    lpublisher = publisher.lower()

    context = {
        'games': games,
        'search_term': query,
    }

    return render(request, f'products/{lpublisher}_games.html', context)


def game_details(request, game_id):
    """
    A view to show an indidvidual game on the site.
    """
    game = get_object_or_404(Game, pk=game_id)

    context = {
        'game': game,
    }

    return render(request, 'products/game_details.html', context)
