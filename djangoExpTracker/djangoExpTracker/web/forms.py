import os

from django import forms

from djangoExpTracker.web.models import Profile, Expense


class CreateProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class EditProfileFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileFrom(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.profile_image.path
        if commit:
            self.instance.delete()
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateExpenseFrom(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class EditExpenseFrom(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DeleteExpenseFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        # return self.instance

    class Meta:
        model = Expense
        fields = ['title', 'description', 'expense_image', 'price']
