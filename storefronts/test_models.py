"""
Tests the models for the storefronts app.
"""
# pylint: disable=no-member
from django.test import TestCase
from django.contrib.auth.models import User
from .models import StoreFront


class TestStoreFrontModel(TestCase):
    """
    Test models in Storefront app
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

        self.test_storefront = StoreFront.objects.create(
            name='testStorefront',
            user=self.test_user,
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

    def test_storefront_string_method_returns_title(self):
        """
        Tests string method for Storefront class
        """
        self.assertEqual(str(self.test_storefront), 'testStorefront')

    def test_storefront_instantiation_(self):
        """
        Tests that the parameters to establish a storefront are functioning as
        expected.
        """
        self.assertIsInstance(self.test_storefront, StoreFront)
