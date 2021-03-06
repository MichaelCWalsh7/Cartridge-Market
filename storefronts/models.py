"""
Models defining user profiles
"""
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class StoreFront(models.Model):
    """
    A strorefront model for users to inform potential clients about the
    listings they have available, their location and other information about
    them.
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number1 = models.CharField(max_length=20, null=False, blank=False)
    contact_number2 = models.CharField(  # noqa: DJ01
        max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(  # noqa: DJ01
        max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(  # noqa: DJ01
        max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(  # noqa: DJ01
        max_length=20, null=True, blank=True)
    image_url = models.CharField(  # noqa: DJ01
        max_length=254, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/storefront-images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)  # noqa: DJ01
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """
        Returns the name of the storefront
        """
        return self.name
