"""
Tests the views for the products app.
"""
# pylint: disable=no-member
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from storefronts.models import StoreFront
from listings.models import Listing
from .models import Publisher, Console, Genre, Game
from .forms import GameForm


class TestProductViews(TestCase):
    """
    Tests the views for the products app.
    """
    def setUp(self):
        """
        Instantiate objects for testing.
        """
        self.test_user1 = User.objects.create_superuser(
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
            name='Nintendo',
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

        self.test_form = GameForm()

        self.test_game1 = Game.objects.create(
            publisher=self.test_publisher,
            console=self.test_console,
            genre=self.test_genre,
            sku='FG-1',
            name='testGame',
            description='test',
            image_url='test',
            image='test',
            release_year='1997',
            multiplayer=True,
            rating=100,
            developer='test',
        )

        self.test_game2 = Game.objects.create(
            publisher=self.test_publisher,
            console=self.test_console,
            genre=self.test_genre,
            sku='FG-2',
            name='testGame',
            description='test',
            image_url='test',
            image='test',
            release_year='1997',
            multiplayer=True,
            rating=100,
            developer='test',
        )

        self.test_game3 = Game.objects.create(
            publisher=self.test_publisher,
            console=self.test_console,
            genre=self.test_genre,
            sku='FG-3',
            name='testGame',
            description='test',
            image_url='test',
            image='test',
            release_year='1997',
            multiplayer=True,
            rating=100,
            developer='test',
        )

        self.test_game4 = Game.objects.create(
            publisher=self.test_publisher,
            console=self.test_console,
            genre=self.test_genre,
            sku='FG-4',
            name='testGame',
            description='test',
            image_url='test',
            image='test',
            release_year='1997',
            multiplayer=True,
            rating=100,
            developer='test',
        )

    def test_all_games_view(self):
        """
        Tests the all_games view.
        """
        # Check the all games page exists
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

        # Check that all games view is using the correct template
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'products/all_games.html')

    def test_publisher_games_view(self):
        """
        Tests the publisher_games views.
        """
        # Check the all games page exists
        response = self.client.get(
            f'/products/publisher/{self.test_publisher.name}/')
        self.assertEqual(response.status_code, 200)

        # Check that all games view is using the correct template
        response = self.client.get(
            f'/products/publisher/{self.test_publisher.name}/')
        self.assertTemplateUsed(response, 'products/nintendo_games.html')

    def test_game_details_view(self):
        """
        Tests the game_details view.
        """
        # Check the all games page exists
        response = self.client.get(f'/products/{self.test_game.id}/')
        self.assertEqual(response.status_code, 200)

        # Check that all games view is using the correct template
        response = self.client.get(f'/products/{self.test_game.id}/')
        self.assertTemplateUsed(response, 'products/game_details.html')

    def test_add_game_views(self):
        """
        Tests the add_game view
        """
        # Check if non-users can add a game
        response = self.client.get('/products/add_game/')
        self.assertEqual(response.status_code, 302)

        # Check if non superusers can add a game
        self.client.force_login(self.test_user2)
        response = self.client.get('/products/add_game/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), 'Sorry, only an admin is allowed to do that.')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check if superusers can add a game
        self.client.force_login(self.test_user1)
        response = self.client.get('/products/add_game/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_edit_game_views(self):
        """
        Tests the edit_game view
        """
        # Check if non-users can edit a game
        response = self.client.get(f'/products/edit_game/{self.test_game.id}')
        self.assertEqual(response.status_code, 302)

        # Check if non superusers can edit a game
        self.client.force_login(self.test_user2)
        response = self.client.get(f'/products/edit_game/{self.test_game.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), 'Sorry, only an admin is allowed to do that.')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Check if superusers can edit a game
        self.client.force_login(self.test_user1)
        response = self.client.get(f'/products/edit_game/{self.test_game.id}')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_delete_game_view(self):
        """
        Tests the delete game view.
        """
        # Checks that superusers can delete games
        self.client.force_login(self.test_user1)
        response = self.client.get(
            f'/products/delete_game/{self.test_game.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'The game has been removed.')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Checks that non-registered users can't delete games.
        response = self.client.get(
            f'/products/delete_game/{self.test_game.id}')
        self.assertIsInstance(self.test_game, Game)
