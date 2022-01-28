"""
Urls for the listings app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('add_listing/', views.add_listing, name='add_listing'),
    path('listing/<listing_id>', views.listing, name='listing'),
    path('listings_by_game/<game_id>', views.listings_by_game,
         name='listings_by_game'),
    path('edit_listing/<listing_id>', views.edit_listing, name='edit_listing'),
    path('delete_listing/<listing_id>', views.delete_listing,
         name='delete_listing'),
]
