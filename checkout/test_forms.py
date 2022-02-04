"""
Tests the forms for the checkout app.
"""
from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    Tests that the order form works
    """
    def test_full_name_requirement(self):
        """
        Tests if the form can be submitted without a full name,
        """
        test_form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': 357632138732,
            'street_address1': 'test',
            'town_or_city': 'Test',
            'county': 'test',
            'country': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('full_name', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['full_name'][0], 'This field is required.')

    def test_email_requirement(self):
        """
        Tests if the form can be submitted without a full name,
        """
        test_form = OrderForm({
            'full_name': 'test',
            'email': '',
            'phone_number': 357632138732,
            'street_address1': 'test',
            'town_or_city': 'Test',
            'county': 'test',
            'country': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('email', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['email'][0], 'This field is required.')

    def test_phone_number_requirement(self):
        """
        Tests if the form can be submitted without a full name,
        """
        test_form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '',
            'street_address1': 'test',
            'town_or_city': 'Test',
            'county': 'test',
            'country': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('phone_number', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['phone_number'][0], 'This field is required.')

    def test_street_address1_requirement(self):
        """
        Tests if the form can be submitted without a full name,
        """
        test_form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': 357632138732,
            'street_address1': '',
            'town_or_city': 'Test',
            'county': 'test',
            'country': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('street_address1', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_requirement(self):
        """
        Tests if the form can be submitted without a full name,
        """
        test_form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': 357632138732,
            'street_address1': 'test',
            'town_or_city': '',
            'county': 'test',
            'country': 'test',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('town_or_city', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['town_or_city'][0], 'This field is required.')

    def test_country_requirement(self):
        """
        Tests if the form can be submitted without a full name,
        """
        test_form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': 357632138732,
            'street_address1': 'test',
            'town_or_city': 'Test',
            'county': 'test',
            'country': '',
        })
        self.assertFalse(test_form.is_valid())
        self.assertIn('country', test_form.errors.keys())
        self.assertEqual(
            test_form.errors['country'][0], 'This field is required.')

    def test_fields_are_correct_in_meta_class(self):
        """
        Check that the correct form fields are visible to user
        """
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number', 'street_address1',
            'street_address2', 'town_or_city', 'postcode', 'country',
            'county',
        ))
