"""
Contains the forms for the profiles app.
"""
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Generates the form the user will complete at checkout.
    """
    class Meta:
        """
        Informs django of the model being drawn from, and the fields
        to be rendered.
        """
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated labels and sets
        autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Post/Zip Code',
            'default_town_or_city': 'Town/City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State, Region, Province',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]}*'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'border-black \
                    rounded-0 profile-form-input'
                self.fields[field].label = False
