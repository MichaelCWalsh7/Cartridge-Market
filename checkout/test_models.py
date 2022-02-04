"""
Tests the models for the checkout app.
"""
# pylint: disable=no-member
from django.test import TestCase
from .models import Order


class TestOrderModels(TestCase):
    """
    Tests that order models work correctly
    """
    def setUp(self):
        """
        Instantiate objects for testing.
        """
        Order.objects.create(
            full_name='test',
            email='test@test.com',
            phone_number=3546874324,
            street_address1='test',
            town_or_city='test',
            country='Albania',
        )

    def test_order_string_method_returns_order_number(self):
        """
        Test string method for Order class
        """
        order_number = Order.objects.create(order_number='test')
        self.assertEqual(str(order_number), 'test')
