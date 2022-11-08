import random

from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from DjangoCBV_Lab.web.models import Employee


# Create your views here.

def index():
    pass


# class IndexView:
#     def __init__(self, ):
#         self.values = [random.randint(1, 15), ]
#
#     @classmethod
#     def get_view(cls):
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'It Works: {self.values}')
#
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15, 30))
class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'CBV'
        }
        return render(request, 'index.html', context)

    def post(self, request):
        pass


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'

    extra_context = {'title': 'TemplateView'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context


class IndexViewWithListView(views.ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employees'
    extra_context = {'title': 'TemplateView'}

    #  if you want to search
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     pattern = self.__get_pattern()
    #     if pattern:
    #         queryset = queryset.filter(first_name__icontains=pattern.lower())
    #     queryset = queryset.order_by('first_name')
    #
    #     return queryset

    def __get_pattern(self):
        return self.request.GET.get('pattern', None)


class EmployeeDetailsView(views.DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employees/detail.html'


class EmployeeCreateView(views.CreateView):
    template_name = 'employees/create.html'
    model = Employee
    fields = '__all__'

    # success_url = '/'

    def get_success_url(self):
        print(self.kwargs)
        created_object = self.object
        return reverse_lazy('employee details', kwargs={'pk': created_object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field_name, field_object in form.fields.items():
            field_object.widget.attrs['placeholder'] = 'Enter ' + field_name.replace('_', ' ')
        return form


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/create.html'

    def get_success_url(self):
        print(self.kwargs)
        created_object = self.object
        return reverse_lazy('employee details', kwargs={'pk': created_object.pk})

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     for field_name, field_object in form.fields.items():
    #         field_object.widget.attrs['plac
