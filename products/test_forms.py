"""
Tests the forms for the products app.
"""
# pylint: disable=no-member
from django.test import TestCase
from .forms import GameForm
from .models import Publisher, Console, Genre


class TestGameForm(TestCase):
    """
    Tests that the game form works
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

    def test_name_requirement(self):
        """
        Tests if the form can be submitted without a name,
        """
        test_form = GameForm({
            'name': '',
            'release_year': 1999,
            'multiplayer': True,
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('name', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['name'][0], 'This field is required.')

    def test_release_year_requirement(self):
        """
        Tests if the form can be submitted without a release_year,
        """
        test_form = GameForm({
            'name': 'test',
            'release_year': '',
            'multiplayer': True,
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('release_year', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['release_year'][0], 'This field is required.')
