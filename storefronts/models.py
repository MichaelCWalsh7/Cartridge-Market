"""
Models defining user profiles
"""
# pylint: disable=no-member,unused-argument,invalid-str-returned
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)  # noqa: DJ01
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        """
        Returns the name of the storefront
        """
        return self.name


@receiver(post_save, sender=StoreFront)
def create_or_update_storefront(sender, instance, created, **kwargs):
    """
    Create or update the storefront
    """
    if created:
        StoreFront.objects.create(storefront=instance)
    # For existing stores, the data is merely saved
    instance.storefront.save()
