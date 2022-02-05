"""
Tests the views for the profiles app.
"""
# pylint: disable=no-member
from django.test import TestCase
from django.contrib.auth.models import User

from checkout.models import Order


class TestProfilesViews(TestCase):
    """
    Test profiles page views
    """
    def setUp(self):
        """
        Instantiate objects for testing.
        """
        self.test_user = User.objects.create(
            username='testuser',
            email='test@testviews.com',
            password='testpassword',
        )

        self.test_order = Order.objects.create(
            order_number='35743246'
        )

    def test_profile_view(self):
        """
        Tests the profile view.
        """
        # Checks that logged in users can see thier profile
        self.client.force_login(self.test_user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        # Checks that the correct template is being used
        self.assertTemplateUsed('profiles/profile.html')
        self.client.logout()

        # Checks that non-logged in users are asked to log in
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        # Checks that the correct template is being used
        self.assertTemplateUsed('accounts/login/')

    def test_order_history_view(self):
        """
        Tests the order_history view.
        """
        # Checks that users can see their order history page
        self.client.force_login(self.test_user)
        response = self.client.get(
            f'/profile/order_history/{self.test_order.order_number}')
        self.assertEqual(response.status_code, 200)

        # Checks that the correct template is being used
        response = self.client.get(
            f'/profile/order_history/{self.test_order.order_number}')
        self.assertTemplateUsed('checkout/checkout_success.html')
