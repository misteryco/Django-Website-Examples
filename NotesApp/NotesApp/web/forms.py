from django import forms

from NotesApp.web.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['image_URL'].label = "Link to Profile Image"

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
            Note.objects.all().delete()
        return self.instance


class BaseNoteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].label = "Link to Image"

    class Meta:
        model = Note
        fields = ('title', 'content', 'image_url')


class CreateNoteForm(BaseNoteForm):
    pass


class EditNoteForm(BaseNoteForm):
    pass


class DeleteNoteForm(BaseNoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_url'].label = "Link to Image"
        for field, field_object in self.fields.items():
            field_object.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
