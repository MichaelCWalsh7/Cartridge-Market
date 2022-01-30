"""
Views defined for the 'products' app
"""
# pylint: disable=no-member
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from products.models import Game, Genre
from listings.models import Listing
from .forms import GameForm


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

    all_listings = Listing.objects.all()
    listings = all_listings.filter(game=game_id)

    context = {
        'game': game,
        'listings': listings,
    }

    return render(request, 'products/game_details.html', context)


@login_required
def add_game(request):
    """
    A view for users to create game on the site.
    """
    user = request.user
    if not user.is_superuser:
        messages.error(request, "Sorry, only an admin is allowed to do that.")
        return reverse(redirect('home'))

    if request.method == 'POST':
        form = GameForm()
        if form.is_valid():
            user = request.user
            image_url = request.POST.get('image_url')
            game = form.save(commit=False)
            game.image_url = image_url
            game.save()
            messages.success(request, "Game uploaded successfully!")
            return redirect(reverse('game_details', args=[game.id]))
        else:
            messages.error(request, 'Failed to add game. Please ensure \
                your form is valid.')
    else:
        form = GameForm()

    games = Game.objects.all()
    genres = Genre.objects.all()
    nintendo_games = games.filter(publisher__name='Nintendo')
    sony_games = games.filter(publisher__name='Sony')
    sega_games = games.filter(publisher__name='Sega')
    atari_games = games.filter(publisher__name='Atari')

    template = 'products/add_game.html'
    context = {
        'games': games,
        'genres': genres,
        'nintendo_games': nintendo_games,
        'sony_games': sony_games,
        'sega_games': sega_games,
        'atari_games': atari_games,
        'form': form,
    }
    return render(request, template, context)
