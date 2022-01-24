"""
Urls for the listings app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('add_listing/', views.add_listing, name='add_listing'),
]