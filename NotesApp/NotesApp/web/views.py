from django.shortcuts import render, redirect

from NotesApp.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm, DeleteProfileForm
from NotesApp.web.models import Profile, Note


# def delete_profile_and_notes(pk):
#     Profile.objects.filter(pk=pk).delete()
#     Note.objects.all().delete()
#     return redirect('home page')


def get_profile():
    profile_data = Profile.objects.first()
    if profile_data:
        return profile_data


def home_page(request):
    profile_data = get_profile()
    notes = Note.objects.all()
    if not profile_data:
        return redirect('profile create')
    context = {
        'profile_data': profile_data,
        'notes': notes
    }
    return render(request, 'home-with-profile.html', context=context)


def add_note(request):
    if request.method == "POST":
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateNoteForm()
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context=context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditNoteForm(instance=note)
    context = {
        'form': form
    }
    return render(request, 'note-edit.html', context=context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'form': form
    }
    return render(request, 'note-delete.html', context=context)


def details_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = {'note': note}
    return render(request, 'note-details.html', context=context)


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
    return render(request, 'home-no-profile.html', context=context)


def profile_view(request):
    profile_data = Profile.objects.first()
    notes_count = Note.objects.count
    # if request.method == 'POST':
    #     form = DeleteProfileForm(request.POST, instance=profile_data)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home page')
    # else:
    #     form = DeleteProfileForm(instance=profile_data)
    context = {
        'profile_data': profile_data,
        'notes_count': notes_count,
        # 'delete_all': delete_profile_and_notes(pk=profile_data.pk)
    }
    return render(request, 'profile.html', context=context)


def profile_delete(request, pk):
    notes = Note.objects.all()
    profile_data = Profile.objects.filter(pk=pk).get()
    notes.delete()
    profile_data.delete()
    return redirect('home page')
