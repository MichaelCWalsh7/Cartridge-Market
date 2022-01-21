"""
Register the storefronts modules so that they can be used in site admin
"""
from django.contrib import admin
from .models import StoreFront


class StoreFrontAdmin(admin.ModelAdmin):
    """
    Defines the order model in the admin.
    """
    model = StoreFront
    readonly_fields = ('user',)

    fields = ('name', 'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 'country',
              'postcode', 'description', 'image_url', 'image',)


admin.site.register(StoreFront)
