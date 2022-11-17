from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic as view

from usersdemos2.auth_app.models import AppUser


# Create your views here.

class UsersListView(auth_mixins.LoginRequiredMixin, view.ListView):
    model = User
    template_name = 'web/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['has_email'] = AppUser.has_email(self.request.user)
        print(self.request.user.__class__)
        return context
