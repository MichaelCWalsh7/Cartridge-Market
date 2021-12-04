
"""
This is where the data schema for the products available on the site will be
initialized, it includes the 4 brands available, their games and consoles.
"""
# pylint: disable=missing-function-docstring,invalid-str-returned
from django.db import models


class Brand(models.Model):
    """
    Here, the four available brands on the website are initialized, they also
    act as psuedo-categories.
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501

    # The below lines converts the object into a string to more easily
    # manage it.
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Console(models.Model):
    """
    Here, any consoles that the store supports are initialized, they also act
    as a kind of psuedo-subcategory
    """
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image_url = models.URLField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    image = models.ImageField(null=True, blank=True)
    release_year = models.IntegerField()
    controller_ports = models.IntegerField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Here, the genres of games on the website are initialized, they also act as
    psuedo-categories.
    """
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Game(models.Model):
    """
    Here, the data schema for 'games', the main product of the site are
    intialized.
    """
    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL
    )
    console = models.ForeignKey(
        'Console', null=True, blank=True, on_delete=models.SET_NULL
    )
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    release_year = models.IntegerField()
    multiplayer = models.BooleanField()
    image_url = models.URLField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
