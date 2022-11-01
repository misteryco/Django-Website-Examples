from django import forms

from CarCollectionApp.web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Car.objects.all().delete()
        return self.instance


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CreateCarForm(BaseCarForm):
    pass


class EditCarForm(BaseCarForm):
    pass


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_object in self.fields.items():
            field_object.widget.attrs['disabled'] = 'disabled'
            field_object.required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
