
# forms.py
from django import forms
from album import models


class AlbumForm(forms.ModelForm):
    """Form for album creation."""

    class Meta:
        model = models.Album
        fields = ['user', 'name', 'public']
