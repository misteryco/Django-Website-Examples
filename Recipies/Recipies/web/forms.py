from django import forms

from Recipies.web.models import Recipe


class BaseRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class CreateRecipeForm(BaseRecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Recipe Title'
        for field_name, field_object in self.fields.items():
            if field_name in ("image_url", 'description'):
                field_object.widget.attrs['placeholder'] = field_object.label
                field_object.required = False


class EditRecipeForm(BaseRecipeForm):
    pass


class DeleteRecipeForm(BaseRecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.fields)  - print all form fields
        for field_name, field_object in self.fields.items():
            if field_name in ("title", 'description'):
                field_object.widget.attrs['disabled'] = 'disabled'
                field_object.required = False
            # print(f'{field_name} - {field_object}')
        # if you want to control them one by one use following syntax
        self.fields['ingredients'].widget.attrs['disabled'] = 'disabled'
        self.fields['ingredients'].required = False

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
