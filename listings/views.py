"""
Views for the listings app.
"""
# pylint: disable=no-member,redefined-outer-name

from datetime import date

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Game

from .models import Listing
from .forms import ListingForm


@login_required
def add_listing(request):
    """
    A view for users to create a listing on the site.
    """
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            storefront = user.storefront
            image_url = request.POST.get('image_url')
            today = date.today()
            today_dd_mm_yy = today.strftime("%d/%m/%Y")
            listing = form.save(commit=False)
            listing.image_url = image_url
            game_id = request.POST.get('game')
            game = get_object_or_404(Game, pk=game_id)
            listing.game = game
            listing.storefront = storefront
            listing.date = today_dd_mm_yy
            listing.save()
            messages.success(request, "Listing uploaded successfully!")
            return redirect(reverse('listing', args=[listing.id]))
        else:
            messages.error(request, 'Failed to add listing. Please ensure \
                your form is valid.')
    else:
        form = ListingForm()

    games = Game.objects.all()
    nintendo_games = games.filter(publisher__name='Nintendo')
    sony_games = games.filter(publisher__name='Sony')
    sega_games = games.filter(publisher__name='Sega')
    atari_games = games.filter(publisher__name='Atari')

    form = ListingForm()

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


def listing(request, listing_id):
    """
    A view to display a listing on the website
    """
    listing = get_object_or_404(Listing, pk=listing_id)

    template = 'listings/listing.html'
    context = {
        'listing': listing
    }
    return render(request, template, context)
