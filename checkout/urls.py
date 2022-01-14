"""
List of urls for the checkout app
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
]
