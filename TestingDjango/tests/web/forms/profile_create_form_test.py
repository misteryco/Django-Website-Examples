from django.test import TestCase

from TestingDjango.web.forms import ProfileCreateForm


class ProfileCreateFormTest(TestCase):
    def test_profile_create_form__disabled_fields__when_All_to_ne_disabled(self):
        form = ProfileCreateForm()
        disabled_fields = {
            name: field.widget.attrs[ProfileCreateForm.disabled_attr_name]
            for name, field in form.fields.items()}

        self.assertEqual(ProfileCreateForm.disabled_attr_name,
                         disabled_fields['name']
                         )
        self.assertEqual(ProfileCreateForm.disabled_attr_name,
                         disabled_fields['age']
                         )
        self.assertEqual(ProfileCreateForm.disabled_attr_name,
                         disabled_fields['egn']
                         )

    def test_profile_create_form__disabled_fields__when_name_is_disabled(self):
        ProfileCreateForm.disabled_fields = ('name',)
        # Monkey patching
        form = ProfileCreateForm()

        disabled_fields = {
            name: field.widget.attrs[ProfileCreateForm.disabled_attr_name]
            for name, field in form.fields.items()}

        self.assertEqual(ProfileCreateForm.disabled_attr_name,
                         disabled_fields['name']
                         )
        self.assertEqual(ProfileCreateForm.disabled_attr_name,
                         disabled_fields['age']
                         )
        self.assertEqual(ProfileCreateForm.disabled_attr_name,
                         disabled_fields['egn']
                         )
