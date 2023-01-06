"""
URL mappings
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from apialbums import views

router = DefaultRouter()
router.register('api/albums', views.AlbumViewSet)

app_name = 'apialbums'

urlpatterns = [
    path('', include(router.urls))
]
