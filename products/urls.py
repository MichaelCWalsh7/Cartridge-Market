"""
List of urls for the Products app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_games, name='all_games'),
    path('nintendo/', views.nintendo_games, name='nintendo_games'),
    path('sega/', views.sega_games, name='sega_games'),
    path('sony/', views.sony_games, name='sony_games'),
    path('atari/', views.atari_games, name='atari_games'),
]
