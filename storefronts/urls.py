"""
Urls for the storefronts app.
"""
from django.urls import path
from . import views

urlpatterns = [
     path('preamble/', views.storefront_preamble, name='storefront_preamble'),
     path('storefronts/<storefront_id>', views.storefront, name='storefront'),
     path('add_storefront/', views.add_storefront, name='add_storefront'),
     path('edit_storefront/<int:storefront_id>', views.edit_storefront,
          name='edit_storefront'),
     path('delete_storefront/<int:storefront_id>', views.delete_storefront,
          name='delete_storefront'),
     path('all_storefronts/', views.all_storefronts, name='all_storefronts'),
]
