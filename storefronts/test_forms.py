"""
Tests the forms for the profiles app.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from .forms import StoreFrontForm


class TestUserProfileForm(TestCase):
    """
    Tests that the profile form works.
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

    def test_name_requirement(self):
        """
        Tests that the name field is required.
        """
        test_form = StoreFrontForm({
            'name': '',
            'email': 'test',
            'contact_number1': 3543873248,
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'Albania',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('name', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['name'][0], 'This field is required.')

    def test_email_requirement(self):
        """
        Tests that the email field is required.
        """
        test_form = StoreFrontForm({
            'name': 'test',
            'email': 'test',
            'contact_number1': 3543873248,
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'Albania',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('email', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['email'][0], 'Enter a valid email address.')

    def test_contact_number1_requirement(self):
        """
        Tests that the contact_number1 field is required.
        """
        test_form = StoreFrontForm({
            'name': 'test',
            'email': 'test',
            'contact_number1': '',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'Albania',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('contact_number1', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['contact_number1'][0], 'This field is required.')

    def test_street_address1_requirement(self):
        """
        Tests that the street_address1 field is required.
        """
        test_form = StoreFrontForm({
            'name': 'test',
            'email': 'test',
            'contact_number1': 3543873248,
            'street_address1': '',
            'town_or_city': 'test',
            'country': 'Albania',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('street_address1', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_requirement(self):
        """
        Tests that the town_or_city field is required.
        """
        test_form = StoreFrontForm({
            'name': 'test',
            'email': 'test',
            'contact_number1': 3543873248,
            'street_address1': 'test',
            'town_or_city': '',
            'country': 'Albania',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('town_or_city', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['town_or_city'][0], 'This field is required.')

    def test_country_requirement(self):
        """
        Tests that the country field is required.
        """
        test_form = StoreFrontForm({
            'name': 'test',
            'email': 'test',
            'contact_number1': 3543873248,
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': '',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('country', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['country'][0], 'This field is required.')
