"""
Contains the forms for the storefronts app.
"""
from django import forms
from .models import StoreFront


class StoreFrontForm(forms.ModelForm):
    """
    Generates the form the user will complete to start a storefront.
    """
    class Meta:
        """
        Informs django of the model being drawn from, and the fields
        to be rendered.
        """
        model = StoreFront
        exclude = ('user', 'rating',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated labels and sets
        autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'contact_number1': 'Contact Number',
            'contact_number2': 'Additional Contact Number',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town/City',
            'county': 'County, State, Region, Province',
            'postcode': 'Post/Zip Code',
            'image_url': 'Image Link',
            'image': 'Image File',
            'description': 'Description',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-black \
                    rounded-0 profile-form-input'
                self.fields[field].label = False
