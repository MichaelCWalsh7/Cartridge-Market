"""
Register the products modules so that they can be used in site admin
"""

from django.contrib import admin
from .models import Game, Genre, Publisher, Console

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Console)
