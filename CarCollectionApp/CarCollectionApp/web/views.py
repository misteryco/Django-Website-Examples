from django.shortcuts import render, redirect

from CarCollectionApp.web.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, EditProfileForm, \
    DeleteProfileForm
from CarCollectionApp.web.models import Car, Profile


# Create your views here.
def get_profile():
    profile = Profile.objects.first()
    if profile:
        return profile


def index(request):
    profile = get_profile()
    context = {
        'profile': profile
    }
    return render(request, template_name='index.html', context=context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
    }
    return render(request, template_name='profile-create.html', context=context)


def catalogue(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_cars = Car.objects.count
    context = {
        'profile': profile,
        'cars': cars,
        'total_cars': total_cars
    }
    return render(request, template_name='catalogue.html', context=context)


def car_create(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateCarForm()
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template_name='car-create.html', context=context)


def car_details(request, pk):
    profile = get_profile()
    car = Car.objects.filter(pk=pk).get()
    context = {
        'car': car,
        'profile': profile,
    }
    return render(request, template_name='car-details.html', context=context)


def car_edit(request, pk):
    profile = get_profile()
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditCarForm(instance=car)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template_name='car-edit.html', context=context)


def car_delete(request, pk):
    profile = get_profile()
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = DeleteCarForm(instance=car)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, template_name='car-delete.html', context=context)


def profile_details(request):
    profile = get_profile()
    total_cars_price = sum([car.price for car in Car.objects.all()])
    context = {
        'profile': profile,
        'total_cars_price': total_cars_price,
    }
    return render(request, template_name='profile-details.html', context=context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, template_name='profile-edit.html', context=context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'profile':profile,
        'form': form
    }
    return render(request, template_name='profile-delete.html', context=context)
