"""
Register the storefronts modules so that they can be used in site admin
"""
from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    """
    Defines the order model in the admin.
    """
    model = Listing
    readonly_fields = ('user', 'storefront',)

    fields = ('title', 'date', 'condition', 'price', 'copies_available',
              'decription', 'image',)


admin.site.register(Listing)
