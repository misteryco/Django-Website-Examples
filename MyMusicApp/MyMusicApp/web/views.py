from django.shortcuts import render, redirect

from MyMusicApp.web.forms import CreateProfileForm, DeleteProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm
from MyMusicApp.web.models import Profile, Album


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile
    # else:
    #     return profile


# Create your views here.
def home_page(request):
    profile = get_profile()
    album_count = len(Album.objects.all())
    albums = Album.objects.all()
    if not profile:
        return redirect('profile create')
    context = {
        'profile': profile,
        'album_count': album_count,
        'albums': albums,
    }
    return render(request, template_name='home-with-profile.html', context=context)


def album_add(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateAlbumForm()
    context = {
        'form': form,
    }
    return render(request, template_name='add-album.html', context=context)


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    context = {
        'album': album
    }
    return render(request, template_name='album-details.html', context=context)


def album_edit(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form
    }
    return render(request, template_name='edit-album.html', context=context)


def album_delete(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {
        'form': form
    }
    return render(request, template_name='delete-album.html', context=context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateProfileForm()
    context = {
        'form': form
    }
    return render(request, template_name='home-no-profile.html', context=context)


def profile_details(request):
    profile = get_profile()
    album_count = len(Album.objects.all())
    context = {
        'profile': profile,
        'album_count': album_count,
    }
    return render(request, template_name='profile-details.html', context=context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, template_name='profile-delete.html', context=context)
