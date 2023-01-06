from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from album import models
from apialbums import serializers


class AlbumViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.AlbumSerialzer
    queryset = models.Album.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for auth user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def list(self, *args, **kwargs):
        self.serializer_class = serializers.AlbumSerialzer
        return viewsets.ModelViewSet.list(self, *args, **kwargs)

    def retrieve(self, request, pk, *args, **kwargs):
        album = models.Album.objects.get(pk=pk)
        images = models.AlbumImage.objects.filter(album=album)

        serializer = serializers.AlbumImageSerialzer(images, many=True)

        return Response(serializer.data)
