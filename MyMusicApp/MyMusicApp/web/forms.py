from django import forms
from django.forms import HiddenInput

from MyMusicApp.web.models import Profile, Album


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        self.instance.delete()
        Album.objects.all().delete()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()

    class Meta:
        model = Album
        fields = '__all__'
