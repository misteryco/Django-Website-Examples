from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.shortcuts import render
from django.views import generic as view

from usersdemos2.auth_app.models import AppUser

UserModel = get_user_model()


# Create your views here.

class UsersListView(auth_mixins.LoginRequiredMixin, view.ListView):
    model = UserModel
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        # context['has_email'] = AppUser.has_email(self.request.user)
        print(self.request.user.__class__)
        return context
