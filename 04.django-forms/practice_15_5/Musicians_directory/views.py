from django.shortcuts import render, redirect
from .forms import Artist_form, Album_form

# Create your views here.
def addMusician(request):
    if request.method == 'POST':
        musicianData = Artist_form(request.POST)
        # print(musicianData)
        if musicianData.is_valid():
            musicianData.save()
            return redirect('add-artist')

    return render(request, 'add_musitian.html', {'data': Artist_form})

def add_album(request):
    if request.method == 'POST':
        albumData = Album_form(request.POST)
        # print(albumData)
        if albumData.is_valid():
            albumData.save()
            return redirect('add_album')

    return render(request, 'add_album.html', {'data': Album_form})
