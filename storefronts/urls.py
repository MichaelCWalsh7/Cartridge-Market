"""
Urls for the profiles app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('preamble/', views.storefront_preamble, name='storefront_preamble'),
]
