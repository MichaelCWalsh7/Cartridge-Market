
"""
This is where the data schema for the products available on the site will be
initialized, it includes the 4 publishers available, their games and consoles.
"""
# pylint: disable=missing-function-docstring,invalid-str-returned
from django.db import models


class Publisher(models.Model):
    """
    Here, the four available publishers on the website are initialized,
    they also act as psuedo-categories.
    """
    name = models.CharField(max_length=254)
    image_url = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    image = models.ImageField(null=True, blank=True)

    # The below lines converts the object into a string to more easily
    # manage it.
    def __str__(self):
        return self.name


class Console(models.Model):
    """
    Here, any consoles that the store supports are initialized, they also act
    as a kind of psuedo-subcategory
    """
    publisher = models.ForeignKey(
        'Publisher', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)  # noqa: DJ01
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    image_url = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    image = models.ImageField(null=True, blank=True)
    release_year = models.IntegerField()
    controller_ports = models.IntegerField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    """
    Here, the genres of games on the website are initialized, they also act as
    categories.
    """
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Game(models.Model):
    """
    Here, the data schema for 'games', the main product of the site are
    intialized.
    """
    publisher = models.ForeignKey(
        'Publisher', null=True, blank=True, on_delete=models.SET_NULL
    )
    console = models.ForeignKey(
        'Console', null=True, blank=True, on_delete=models.SET_NULL
    )
    genre = models.ForeignKey(
        'Genre', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    name = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)  # noqa: DJ01
    developer = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    rating = models.IntegerField(null=True, blank=True)
    release_year = models.IntegerField()
    multiplayer = models.BooleanField()
    image_url = models.CharField(max_length=254, null=True, blank=True)  # noqa: DJ01,E501
    image = models.ImageField(upload_to='images/game-images',
                              null=True, blank=True)

    def __str__(self):
        return self.name
