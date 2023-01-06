from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Album(models.Model):
    """Album Model"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        to_field='username'
    )
    name = models.CharField(max_length=256)
    public = models.BooleanField(default=True)


class AlbumImage(models.Model):
    """Model for Images"""

    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='uploads')