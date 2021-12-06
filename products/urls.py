"""
List of urls for the Products app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_games, name='all_games'),
]
