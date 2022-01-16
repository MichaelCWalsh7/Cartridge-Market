"""
Contains the forms for the checkout app.
"""
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Generates the form the user will complete at checkout.
    """
    class Meta:
        """
        Informs django of the model being drawn from, and the fields
        to be rendered.
        """
        model = Order
        fields = ('full_name', 'email', 'phone_number', 'street_address1',
                  'street_address2', 'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated labels and sets
        autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Post/Zip Code',
            'town_or_city': 'Town/City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State, Region, Province',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'stripe-style-input'
                self.fields[field].label = False
