"""
Views defined for the 'cart' app
"""
# pylint: disable=no-member,attribute-defined-outside-init
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Publisher, Console, Genre, Game
from storefronts.models import StoreFront
from listings.models import Listing


class TestCartViews(TestCase):
    """
    Test views in cart app
    """
    def setUp(self):
        """
        Instantiate objects for testing.
        """
        self.test_user = User.objects.create_user(
            username='testuser',
            email='test@testviews.com',
            password='testpassword',
        )

        self.test_publisher = Publisher.objects.create(
            name='testPublisher',
            image_url='test',
            image='test',
        )

        self.test_console = Console.objects.create(
            publisher=self.test_publisher,
            sku='test',
            name='testConsole',
            description='test',
            price=25.52,
            image_url='test',
            image='test',
            release_year='1997',
            controller_ports=2,
        )

        self.test_genre = Genre.objects.create(
            name='Test'
        )

        self.test_game = Game.objects.create(
            publisher=self.test_publisher,
            console=self.test_console,
            genre=self.test_genre,
            sku='test',
            name='testGame',
            description='test',
            image_url='test',
            image='test',
            release_year='1997',
            multiplayer=True,
            rating=100,
            developer='test',
        )

        self.test_storefront = StoreFront.objects.create(
            name='testStorefront',
            user=self.test_user,
            email='test@test.com',
            contact_number1=3574354,
            contact_number2=35468432,
            street_address1='test',
            street_address2='test',
            town_or_city='test',
            county='test',
            country='Albania',
            postcode='3574353d',
            image_url='test',
            image='test',
            description='test',
            rating=100,
        )

        self.test_listing = Listing.objects.create(
            title='testListing',
            game=self.test_game,
            storefront=self.test_storefront,
            price=19.99,
            condition='test',
            date='date',
            image_url='test',
            image='test',
            description='test',
            copies_available=7,
        )

        self.quantity = 2

    def test_view_cart_view(self):
        """
        Test that cart is viewable
        """
        response = self.client.get('/cart/')
        self.assertTrue(response.status_code, 200)
        self.assertTemplateUsed('cart/cart.html')

    def test_add_to_cart_view(self):
        """
        Test that items can be added to the cart
        """
        cart_data = {
            'listing': Listing.objects.get(pk=self.test_listing.id),
            'quantity': int(self.quantity),
            'redirect_url': f'/listing/{self.test_listing.id}/'
        }

        response = self.client.post(
            f'/cart/add/{self.test_listing.id}/', cart_data)
        self.assertEqual(response.status_code, 302)
