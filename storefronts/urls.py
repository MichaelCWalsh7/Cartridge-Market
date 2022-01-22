"""
Urls for the storefronts app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('preamble/', views.storefront_preamble, name='storefront_preamble'),
]
