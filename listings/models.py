"""
Models defining user profiles
"""
# pylint: disable=no-member,unused-argument,invalid-str-returned
from django.db import models

from products.models import Game
from storefronts.models import StoreFront


class Listing(models.Model):
    """
    The model defining what data attributes a listing uploaded onto the site
    has. These listings will the objects that users are able to purchase and
    add to their cart.
    """
    title = models.CharField(max_length=254, null=False, blank=False)
    game = models.ForeignKey(Game, null=False, blank=False,
                             on_delete=models.CASCADE)
    storefront = models.ForeignKey(StoreFront, null=False, blank=False,
                                   on_delete=models.CASCADE)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False
    )
    sku = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    condition = models.CharField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    image_url = models.CharField(  # noqa: DJ01
        max_length=254, null=True, blank=True)
    image = models.ImageField(
        upload_to='images/listing-images', null=True, blank=True)
    description = models.TextField(null=True, blank=True)  # noqa: DJ01
    copies_available = models.IntegerField(null=False, blank=False)

    def __str__(self):
        """
        Returns the title of the listing
        """
        return self.title
