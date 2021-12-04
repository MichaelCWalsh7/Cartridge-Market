"""
Register the products modules so that they can be used in site admin
"""

from django.contrib import admin
from .models import Game, Genre, Brand, Console

admin.site.register(Game)
admin.site.register(Genre)
admin.site.register(Brand)
admin.site.register(Console)
