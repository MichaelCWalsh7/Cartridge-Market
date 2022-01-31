"""
Views defined for the 'products' app
"""
# pylint: disable=no-member
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from products.models import Game, Genre, Publisher, Console
from listings.models import Listing
from .forms import GameForm


def all_games(request):
    """
    A view to show all games currently available on the site.
    """
    games = Game.objects.all()
    genres = Genre.objects.all()
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
            else:
                sortkeys = False
            if sortkeys:
                category = sortkeys[0]
                games = games.order_by(f'{direction}{category}')

    context = {
        'games': games,
        'genres': genres,
        'search_term': query,

    }

    return render(request, 'products/all_games.html', context)


def publisher_games(request, publisher):
    """
    A view to show all games currently available on the site, ordered and
    styled by publihser.
    """
    games = Game.objects.filter(publisher__name=publisher)
    genres = Genre.objects.all()
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
            else:
                sortkeys = False
            if sortkeys:
                category = sortkeys[0]
                games = games.order_by(f'{direction}{category}')

    context = {
        'games': games,
        'genres': genres,
        'search_term': query,

    }

    lpublisher = publisher.lower()
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
        form = GameForm(request.POST, request.FILES)
        publishers = Publisher.objects.all()
        publisher_id = request.POST.get('publisher')
        publisher = get_object_or_404(Publisher, pk=publisher_id)
        genre_id = request.POST.get('genre')
        if publisher.name == "Nintendo":
            console = get_object_or_404(Console, name="Nintendo 64")
        elif publisher.name == "Sony":
            console = get_object_or_404(Console, name="PlayStation")
        elif publisher.name == "Sega":
            console = get_object_or_404(Console, name="Sega Genesis")
        elif publisher.name == "Atari":
            console = get_object_or_404(Console, name="Atari 2600")

        if form.is_valid():
            game = form.save(commit=False)
            game.sku = "Placeholder Sku"
            game.rating = 0
            game.genre = get_object_or_404(Genre, pk=genre_id)
            game.image_url = request.POST["image_url"]
            game.description = request.POST["description"]
            game.release_year = request.POST["release_year"]
            game.developer = request.POST["developer"]
            game.name = request.POST["name"]
            game.console = console
            game.save()
            messages.success(request, "The game has been added successfully.")
            return redirect(reverse('game_details', args=[game.id]))
        else:
            messages.error(request, 'Failed to add game. Please ensure \
                your form is valid.')
    else:
        form = GameForm()

    games = Game.objects.all()
    genres = Genre.objects.all()
    publishers = Publisher.objects.all()

    template = 'products/add_game.html'
    context = {
        'games': games,
        'genres': genres,
        'publishers': publishers,
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_game(request, game_id):
    """
    A view for users to edit games on the site.
    """
    user = request.user
    if not user.is_superuser:
        messages.error(request, "Sorry, only an admin is allowed to do that.")
        return reverse(redirect('home'))
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        publishers = Publisher.objects.all()
        publisher_id = request.POST.get('publisher')
        publisher = get_object_or_404(Publisher, pk=publisher_id)
        genre_id = request.POST.get('genre')
        if publisher.name == "Nintendo":
            console = get_object_or_404(Console, name="Nintendo 64")
        elif publisher.name == "Sony":
            console = get_object_or_404(Console, name="Playstation")
        elif publisher.name == "Sega":
            console = get_object_or_404(Console, name="Sega Genesis")
        elif publisher.name == "Atari":
            console = get_object_or_404(Console, name="Atari 2600")

        if form.is_valid():
            image_url_field = request.POST.get('image_url')
            if image_url_field is None:
                image_url = game.image_url
            else:
                image_url = image_url_field
            game.image_url = image_url
            game = form.save(commit=False)
            game.sku = "Placeholder Sku"
            game.rating = 0
            game.genre = get_object_or_404(Genre, pk=genre_id)
            game.description = request.POST["description"]
            game.release_year = request.POST["release_year"]
            game.developer = request.POST["developer"]
            game.name = request.POST["name"]
            game.console = console
            game.save()
            messages.success(request, "The game has been edited successfully.")
            return redirect(reverse('game_details', args=[game.id]))
        else:
            messages.error(request, 'Failed to edit game. Please ensure \
                your form is valid.')
    else:
        form = GameForm(instance=game)

    genres = Genre.objects.all()
    publishers = Publisher.objects.all()

    template = 'products/edit_game.html'
    context = {
        'game': game,
        'genres': genres,
        'publishers': publishers,
        'form': form,
    }
    return render(request, template, context)


@login_required
def delete_game(request, game_id):
    """
    Allows users to delete games on the website.
    """
    user = request.user
    game = get_object_or_404(Game, pk=game_id)
    if not user.is_superuser:
        messages.error(request, "Sorry, only an admin is allowed to do that.")
        return reverse(redirect('home'))
    game.delete()
    messages.success(request, 'The game has been removed.')
    return redirect(reverse('home'))
