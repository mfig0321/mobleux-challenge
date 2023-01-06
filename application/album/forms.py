
# forms.py
from django import forms
from album import models


class AlbumForm(forms.ModelForm):
    """Form for album creation."""

    class Meta:
        model = models.Album
        fields = ['name', 'public']


class AlbumImageForm(forms.ModelForm):
    """Form for album images"""

    class Meta:
        model = models.AlbumImage
        fields = ['title', 'image']
