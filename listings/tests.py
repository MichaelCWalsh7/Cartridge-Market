# # pylint: disable=no-member,attribute-defined-outside-init
# from django.test import TestCase
# from django.contrib.auth.models import User
# from products.models import Publisher, Console, Genre, Game
# from storefronts.models import StoreFront
# from listings.models import Listing


# class TestListingModel(TestCase):
#     """
#     Test models in Listings app
#     """
#     def setUp(self):
#         """
#         Instantiate objects for testing.
#         """
#         self.test_user = User.objects.create(
#             username='testuser',
#             email='test@testviews.com',
#             password='testpassword',
#         )

#         self.test_publisher = Publisher.objects.create(
#             name='testPublisher',
#             image_url='test',
#             image='test',
#         )

#         self.test_console = Console.objects.create(
#             publisher=self.test_publisher,
#             sku='test',
#             name='testConsole',
#             description='test',
#             price=25.52,
#             image_url='test',
#             image='test',
#             release_year='1997',
#             controller_ports=2,
#         )

#         self.test_genre = Genre.objects.create(
#             name='Test'
#         )

#         self.test_game = Game.objects.create(
#             publisher=self.test_publisher,
#             console=self.test_console,
#             genre=self.test_genre,
#             sku='test',
#             name='testGame',
#             description='test',
#             image_url='test',
#             image='test',
#             release_year='1997',
#             multiplayer=True,
#             rating=100,
#             developer='test',
#         )

#         self.test_storefront = StoreFront.objects.create(
#             name='testStorefront',
#             user=self.test_user,
#             email='test@test.com',
#             contact_number1=3574354,
#             contact_number2=35468432,
#             street_address1='test',
#             street_address2='test',
#             town_or_city='test',
#             county='test',
#             country='Albania',
#             postcode='3574353d',
#             image_url='test',
#             image='test',
#             description='test',
#             rating=100,
#         )

#         self.test_listing = Listing.objects.create(
#             title='testListing',
#             game=self.test_game,
#             storefront=self.test_storefront,
#             price=19.99,
#             condition='test',
#             date='date',
#             image_url='test',
#             image='test',
#             description='test',
#             copies_available=7,
#         )

#     def test_string_method_returns_title(self):
#         "test listing class title returns as string"
#         self.assertIsInstance(self.test_listing.title, "testListing",)
