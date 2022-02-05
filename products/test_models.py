"""
Tests the models for the products app.
"""
# pylint: disable=no-member
from django.test import TestCase
from .models import Publisher, Console, Genre, Game


class TestProductModels(TestCase):
    """
    Tests the models for the products app.
    """
    def setUp(self):
        """
        Instantiate objects for testing.
        """
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

    # Publisher
    def test_publisher_string_method_returns_title(self):
        """
        Tests string method for Publisher class
        """
        self.assertEqual(str(self.test_publisher), 'testPublisher')

    def test_publisher_instantiation_(self):
        """
        Tests that the parameters to establish a publisher are functioning as
        expected.
        """
        self.assertIsInstance(self.test_publisher, Publisher)

    # Console
    def test_console_string_method_returns_title(self):
        """
        Tests string method for Console class
        """
        self.assertEqual(str(self.test_console), 'testConsole')

    def test_console_instantiation_(self):
        """
        Tests that the parameters to establish a console are functioning as
        expected.
        """
        self.assertIsInstance(self.test_console, Console)

    # Genre
    def test_genre_string_method_returns_title(self):
        """
        Tests string method for Genre class
        """
        self.assertEqual(str(self.test_genre), 'Test')

    def test_genre_instantiation_(self):
        """
        Tests that the parameters to establish a genre are functioning as
        expected.
        """
        self.assertIsInstance(self.test_genre, Genre)

    # Game
    def test_game_string_method_returns_title(self):
        """
        Tests string method for Game class
        """
        self.assertEqual(str(self.test_game), 'testGame')

    def test_game_instantiation_(self):
        """
        Tests that the parameters to establish a game are functioning as
        expected.
        """
        self.assertIsInstance(self.test_game, Game)
