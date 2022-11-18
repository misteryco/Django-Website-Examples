from django.shortcuts import render
from django.views import generic as views

from TestingDjango.web.models import Profile


# Create your views here.
class EmployeesListView(views.ListView):
    template_name = 'profiles/list.html'
    model = Profile

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['profiles_count'] = self.object_list.count()
        context['username'] = self.request.user.username or 'Anonymous'

        return context
