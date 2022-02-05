"""
Tests the models for the checkout app.
"""
# pylint: disable=no-member
from django.test import TestCase
from django.contrib.messages import get_messages


class TestCheckoutViews(TestCase):
    """
    Tests that the checkout views work correctly
    """
    def test_checkout_view_url(self):
        """
        Test that the checkout page URL exists
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_empty_cart_error(self):
        """
        Tests that an error message is displayed when cart is empty
        """
        response = self.client.get('/checkout/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "There's nothing in your cart at the moment")
