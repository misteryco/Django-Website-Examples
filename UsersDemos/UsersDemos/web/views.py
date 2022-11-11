from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.views import generic

from UsersDemos.auth_app.models import AppUser

UserModel = get_user_model()


# Create your views here.
class UsersListView(auth_mixins.LoginRequiredMixin, generic.ListView):
    model = UserModel
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context
