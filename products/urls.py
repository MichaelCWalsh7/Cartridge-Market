"""
List of urls for the Products app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_games, name='all_games'),
    path('<game_id>', views.game_details, name='game_details'),
    path('publisher/<publisher>/',
         views.publisher_games, name='publisher_games'
         ),
]
