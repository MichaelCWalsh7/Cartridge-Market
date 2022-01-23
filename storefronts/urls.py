"""
Urls for the storefronts app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('preamble/', views.storefront_preamble, name='storefront_preamble'),
    path('add_storefront/', views.add_storefront, name='add_storefront'),
    path('storefronts/<storefront_id>', views.storefront, name='storefront'),
]
