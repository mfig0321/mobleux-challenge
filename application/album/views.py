from django.shortcuts import render
from django.http import HttpResponseRedirect

from album import forms, models
# Create your views here.


def index(request):
    """View function for home page of site."""

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.save()

            return HttpResponseRedirect('/success/')
  
    else:
        form = forms.AlbumForm()

    return render(request, 'home/index.html', {'form': form})


def save_success(request):
    """View function for save success."""

    return render(request, 'home/success.html')


def my_albums(request):
    """View function for my albums. """
    albums = models.Album.objects.filter(user=request.user)
    context = {'albums': albums}

    return render(request, 'home/myalbums.html', context=context)


def upload_image(request, pk):
    """View function to upload image to album"""

    if request.method == 'POST':
        album = models.Album.objects.get(pk=pk)
        form = forms.AlbumImageForm(request.POST, request.FILES)
        if form.is_valid():
            album_image = form.save(commit=False)
            album_image.album = album
            album_image.save()

            return HttpResponseRedirect('/success/')
  
        context = {'form': form, 'album': album}

    else:
        album = models.Album.objects.get(pk=pk)
        form = forms.AlbumImageForm()
        images = models.AlbumImage.objects.filter(album=album)
        print(images)
        context = {'form': form, 'album': album, 'images': images}

    return render(request, 'album/uploadimage.html', context=context)
