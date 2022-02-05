"""
Tests the views for the storefronts app.
"""
# pylint: disable=no-member
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from .models import StoreFront


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

        self.test_storefront = StoreFront.objects.create(
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

    def test_storefront_preamble_view(self):
        """
        Tests the strorefront preamble view.
        """
        # Checks that the storefront preamble page exists
        self.client.force_login(self.test_user1)
        response = self.client.get('/storefront/preamble/')
        self.assertEqual(response.status_code, 200)

        # Checks that storefront preamble view uses the correct template
        response = self.client.get('/storefront/preamble/')
        self.assertTemplateUsed(response, 'storefronts/preamble.html')
        self.client.logout()

    def test_storefront_view(self):
        """
        Tests the strorefront view.
        """
        # Checks that the storefront page exists
        response = self.client.get(
            f'/storefront/storefronts/{self.test_storefront.id}')
        self.assertEqual(response.status_code, 200)

        # Checks that storefront view uses the correct template
        response = self.client.get(
            f'/storefront/storefronts/{self.test_storefront.id}')
        self.assertTemplateUsed(response, 'storefronts/storefront.html')

    def test_add_storefromt_view(self):
        """
        Tests the add_storefront view.
        """
        # Check if non-users can add a storefront
        response = self.client.get('/storefront/add_storefront/')
        self.assertEqual(response.status_code, 302)

        # Check if registered users can add a storefront
        self.client.force_login(self.test_user2)
        response = self.client.get('/storefront/add_storefront/')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

    def test_edit_storefront_view(self):
        """
        Tests the edit storefront view.
        """
        # Check if non-users can edit a storefront
        response = self.client.get(
            f'/storefront/edit_storefront/{self.test_storefront.id}')
        self.assertEqual(response.status_code, 302)

        # Check if registered users can edit a storefront they own
        self.client.force_login(self.test_user1)
        response = self.client.get(
            f'/storefront/edit_storefront/{self.test_storefront.id}')
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        # Check if registered users can edit a storefront they don't own
        self.client.force_login(self.test_user2)
        response = self.client.get(
            f'/storefront/edit_storefront/{self.test_storefront.id}')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

    def test_delete_storefront_view(self):
        """
        Tests the delete storefront view.
        """
        # Checks that users can delete their storefronts
        self.client.force_login(self.test_user1)
        response = self.client.get(
            f'/storefront/delete_storefront/{self.test_storefront.id}')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Your storefront has been deleted.')
        self.assertEqual(response.status_code, 302)
        self.client.logout()

        # Checks that non-registered users can't delete storefronts.
        response = self.client.get(
            f'/storefront/delete_storefront/{self.test_storefront.id}')
        self.assertIsInstance(self.test_storefront, StoreFront)

    def test_all_storefronts_view(self):
        """
        Tests the all_strorefronts view.
        """
        # Checks that the all_storefronts page exists
        response = self.client.get('/storefront/all_storefronts/')
        self.assertEqual(response.status_code, 200)

        # Checks that storefront view uses the correct template
        response = self.client.get('/storefront/all_storefronts/')
        self.assertTemplateUsed(response, 'storefronts/all_storefronts.html')
