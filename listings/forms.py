"""
Contains the forms for the listings app.
"""
from django import forms
from .models import Listing


class ListingtForm(forms.ModelForm):
    """
    Generates the form the user will complete to post a listing.
    """
    class Meta:
        """
        Informs django of the model being drawn from, and the fields
        to be rendered.
        """
        model = Listing
        exclude = ('storefront', 'game', 'date',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated labels and sets
        autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'price': 'Price',
            'condition': 'Condtion (Mint, Like New, Well Used, etc.)',
            'copies_available': 'Copies Available',
            'image_url': 'Image Link',
            'image': 'Image File',
            'description': 'Add any other details about this listing here',
        }

        self.fields['title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black \
                rounded-0 profile-form-input'
            self.fields[field].label = False
