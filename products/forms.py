"""
Contains the forms for the productss app.
"""
from django import forms
from .models import Game


class GameForm(forms.ModelForm):
    """
    Generates the form the user will complete to upload a game.
    """
    class Meta:
        """
        Informs django of the model being drawn from, and the fields
        to be rendered.
        """
        model = Game
        exclude = ('sku', 'rating',)

    def __init__(self, *args, **kwargs):
        """
        Adds placeholders and classes, removes auto-generated labels and sets
        autofocus on first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'publisher': 'Publisher',
            'console': 'Console',
            'genre': 'Genre',
            'developer': 'Game Developers',
            'condition': 'Condtion (Mint, Like New, Well Used, etc.)',
            'release_year': 'Release Year',
            'image_url': 'Image Link',
            'image': 'Image File',
            'multiplayer': 'Multiplayer',
            'description': 'Add any other details about this game here',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]}*'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black \
                rounded-0 profile-form-input'
            self.fields[field].label = False
