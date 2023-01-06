""""
Serializers for Album APIs
"""

from rest_framework import serializers

from album import models


class AlbumImageSerialzer(serializers.ModelSerializer):
    """Image serializer"""

    class Meta:
        model = models.AlbumImage
        fields = ['title', 'image']


class AlbumSerialzer(serializers.ModelSerializer):
    """Serializer for albums"""

    class Meta:
        model = models.Album
        fields = ['name', 'public']
