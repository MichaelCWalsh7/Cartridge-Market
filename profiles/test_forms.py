"""
Tests the forms for the profiles app.
"""

from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):
    """
    Tests that the profile form works.
    """
    def test_fields_requirement(self):
        """
        Tests if form submits without any fields
        """
        form = {
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_town_or_city': '',
            'default_county': '',
            'default_postcode': '',
        }
        form = UserProfileForm(data=form)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)
