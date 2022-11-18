from django.urls import path

from TestingDjango.web.views import EmployeesListView

urlpatterns = [
    path('', EmployeesListView.as_view(), name='list profiles')
]
