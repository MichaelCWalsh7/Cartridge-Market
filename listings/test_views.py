"""
Tests the views for the listings app.
"""
# pylint: disable=no-member,attribute-defined-outside-init
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from products.models import Publisher, Console, Genre, Game
from storefronts.models import StoreFront
from listings.models import Listing


class TestListingViews(TestCase):
    """
    Test views in Listings app
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

        self.test_listing = Listing.objects.create(
            title='testListing',
            game=self.test_game,
            storefront=self.test_storefront1,
            price=19.99,
            condition='test',
            date='date',
            image_url='test',
            image='test',
            description='test',
            copies_available=7,
        )

    def test_add_listing_view(self):
        """
        Tests the add listing view.
        """

        # Check if non-users can add a listing
        response = self.client.get('/listing/add_listing')
        self.assertEqual(response.status_code, 302)

        # Check if registered users can add a listing
        self.client.force_login(self.test_user1)
        response = self.client.get('/listing/add_listing')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_add_listing_by_game_view(self):
        """
        Tests the add games by listing view
        """
        # Check if non-users can add a listing
        response = self.client.get(
            f'/listing/add_listing_by_game/{self.test_listing.id}')
        self.assertEqual(response.status_code, 302)

        # Check if registered users can add a listing
        self.client.force_login(self.test_user1)
        response = self.client.get(
            f'/listing/add_listing_by_game/{self.test_listing.id}')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_edit_listing_view(self):
        """
        Tests the edit listing view.
        """
        # Check if non-users can edit a listing
        response = self.client.get(
            f'/listing/edit_listing/{self.test_listing.id}')
        self.assertEqual(response.status_code, 302)

        # Check if registered users can edit a listing they own
        self.client.force_login(self.test_user1)
        response = self.client.get(
            f'/listing/edit_listing/{self.test_listing.id}')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check if registered users can edit a listing they don't own
        self.client.force_login(self.test_user2)
        response = self.client.get(
            f'/listing/edit_listing/{self.test_listing.id}')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

    def test_delete_listing_view(self):
        """
        Tests the delete listing view.
        """
        # Checks that users can delete their listings
        self.client.force_login(self.test_user1)
        response = self.client.get(
            f'/listing/delete_listing/{self.test_listing.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Your listing has been removed.')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Checks that non-registered users can't delete listings.
        response = self.client.get(
            f'/listing/delete_listing/{self.test_listing.id}')
        self.assertIsInstance(self.test_listing, Listing)

    def test_listing_view(self):
        """
        Tests the individual listing view
        """
        # Checks that listing view page exists
        response = self.client.get(f'/listing/listing/{self.test_listing.id}')
        self.assertEqual(response.status_code, 200)

        # Checks that listing view uses the correct template
        response = self.client.get(f'/listing/listing/{self.test_listing.id}')
        self.assertTemplateUsed(response, 'listings/listing.html')

    def test_listings_by_game_view(self):
        """
        Tests the games listings view
        """
        # Checks that listing view page exists
        response = self.client.get(
            f'/listing/listings_by_game/{self.test_listing.id}')
        self.assertEqual(response.status_code, 200)

        # Checks that listing view uses the correct template
        response = self.client.get(
            f'/listing/listings_by_game/{self.test_listing.id}')
        self.assertTemplateUsed(response, 'listings/listings_by_game.html')
