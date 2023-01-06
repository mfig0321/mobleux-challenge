from django.shortcuts import render
from django.http import HttpResponseRedirect

from album import forms
# Create your views here.


def index(request):
    """View function for home page of site."""

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/success/')
        
    else:
        form = forms.AlbumForm()

    return render(request, 'home/index.html', {'form': form})


def save_success(request):
    """View function for home page of site."""

    return render(request, 'home/success.html')
