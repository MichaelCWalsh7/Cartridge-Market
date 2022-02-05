"""
Tests the forms for the listings app.
"""
# pylint: disable=no-member
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Publisher, Console, Genre, Game
from storefronts.models import StoreFront
from .forms import ListingForm


class TestListingForm(TestCase):
    """
    Tests that the listing form works
    """
    def setUp(self):
        """
        Instantiate objects for testing.
        """
        self.test_user1 = User.objects.create(
            username='testuser',
            email='test@testviews.com',
            password='testpassword',
        )

        self.test_user2 = User.objects.create(
            username='testuser2',
            email='test2@testviews.com',
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

        self.test_storefront1 = StoreFront.objects.create(
            name='testStorefront',
            user=self.test_user1,
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

        self.test_storefront2 = StoreFront.objects.create(
            name='testStorefront2',
            user=self.test_user2,
            email='test2@test.com',
            contact_number1=357432254,
            contact_number2=354684232,
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

    def test_title_requirement(self):
        """
        Tests if the form can be submitted without a title,
        """
        test_form = ListingForm({
            'title': '',
            'price': 19.99,
            'sku': 'test',
            'condition': 'test',
            'copies_available': 1,
            'county': 'test',
            'country': 'test',
            'image_url': 'test',
            'image': 'test',
            'description': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('title', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['title'][0], 'This field is required.')

    def test_price_requirement(self):
        """
        Tests if the form can be submitted without a price,
        """
        test_form = ListingForm({
            'title': 'test',
            'price': '',
            'sku': 'test',
            'condition': 'test',
            'copies_available': 1,
            'county': 'test',
            'country': 'test',
            'image_url': 'test',
            'image': 'test',
            'description': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('price', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['price'][0], 'This field is required.')

    def test_condition_requirement(self):
        """
        Tests if the form can be submitted without a condition,
        """
        test_form = ListingForm({
            'title': 'test',
            'price': 19.99,
            'sku': 'test',
            'condition': '',
            'copies_available': 1,
            'county': 'test',
            'country': 'test',
            'image_url': 'test',
            'image': 'test',
            'description': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('condition', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['condition'][0], 'This field is required.')

    def test_copies_available_requirement(self):
        """
        Tests if the form can be submitted without a copies_available,
        """
        test_form = ListingForm({
            'title': 'test',
            'price': 19.99,
            'sku': 'test',
            'condition': 'test',
            'copies_available': '',
            'county': 'test',
            'country': 'test',
            'image_url': 'test',
            'image': 'test',
            'description': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('copies_available', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['copies_available'][0], 'This field is required.')
