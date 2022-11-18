from django import forms

from TestingDjango.common.forms.mixins.disabled_form_mixin import DisabledFormMixin
from TestingDjango.web.models import Profile


class ProfileCreateForm(DisabledFormMixin, forms.ModelForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    class Meta:
        model = Profile
        fields = '__all__'
