"""
Models defining user profiles
"""
# pylint: disable=no-member,unused-argument
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default delivery information &
    order history, as well as writing and receiving notifications
    for comments on products.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(  # noqa: DJ01
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(  # noqa: DJ01
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(  # noqa: DJ01
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(  # noqa: DJ01
        max_length=40, null=True, blank=True)
    default_county = models.CharField(  # noqa: DJ01
        max_length=80, null=True, blank=True)
    default_postcode = models.CharField(  # noqa: DJ01
        max_length=20, null=True, blank=True)
    default_country = CountryField(  # noqa: DJ01
        blank_label='Country', null=True, blank=True)

    def __str__(self):
        """
        Returns the username
        """
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    # if created:
    UserProfile.objects.create(user=instance)
    # For existing users, the profile is merely saved
    # instance.userprofile.save()
