from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from GamesPlayApp.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    age = forms.IntegerField(validators=[MinValueValidator(12)])

    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']


class EditProfileForm(forms.ModelForm):
    age = forms.IntegerField(validators=[MinValueValidator(12)])

    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class BaseGameForm(forms.ModelForm):
    rating = forms.FloatField(
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        ])
    max_level = forms.IntegerField(
        validators=[
            MinValueValidator(1)
        ],
    )

    class Meta:
        model = Game
        fields = '__all__'


class CreateGameForm(BaseGameForm):
    pass


class EditGameForm(BaseGameForm):
    pass


class DeleteGameForm(BaseGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_name_object in self.fields.items():
            field_name_object.widget.attrs['disabled'] = 'disabled'
            field_name_object.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
