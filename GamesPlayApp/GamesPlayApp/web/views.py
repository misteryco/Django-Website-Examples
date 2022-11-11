from django.shortcuts import render, redirect

from GamesPlayApp.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from GamesPlayApp.web.models import Profile, Game


def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile


# Create your views here.
def home_page(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, template_name='home-page.html', context=context)


def create_profile(request):
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
    return render(request, template_name='create-profile.html', context=context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, template_name='dashboard.html', context=context)


def create_game(request):
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()
    context = {
        'form': form,
    }
    return render(request, template_name='create-game.html', context=context)


def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    context = {
        'game': game,
    }
    return render(request, template_name='details-game.html', context=context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EditGameForm(instance=game)
    context = {
        'form': form
    }
    return render(request, template_name='edit-game.html', context=context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DeleteGameForm(instance=game)
    context = {
        'form': form
    }

    return render(request, template_name='delete-game.html', context=context)


def details_profile(request):
    profile = get_profile()
    games = Game.objects.all()
    if games:
        average_rating = sum([game.rating for game in games]) / len(games)
    else:
        average_rating = 'You need at least one game to calculate average rating'
    context = {
        'profile': profile,
        'games_count': len(games),
        'average_rating': average_rating
    }
    return render(request, template_name='details-profile.html', context=context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, template_name='edit-profile.html', context=context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form
    }
    return render(request, template_name='delete-profile.html', context=context)
