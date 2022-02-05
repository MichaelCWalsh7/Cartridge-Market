"""
Tests the view for the home app.
"""
# pylint: disable=no-member
from django.test import TestCase


class TestHomeView(TestCase):
    """
    Tests that the home view works correctly
    """
    def test_home_view_url(self):
        """
        Tests that the home page page URL exists

        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
