from django.shortcuts import redirect
from django.urls import path
from django.views import generic as views

from DjangoCBV_Lab.web.views import IndexView, IndexViewWithTemplate, IndexViewWithListView, EmployeeDetailsView, \
    EmployeeCreateView, EmployeeUpdateView

urlpatterns = [
    path('', IndexViewWithListView.as_view()),
    path('create/', EmployeeCreateView.as_view(), name='employee crete'),
    path('edit/<int:pk>', EmployeeUpdateView.as_view(), name='employee edit'),
    path('details/<int:pk>', EmployeeDetailsView.as_view(), name='employee details'),
    path('redirect-to-index/', views.RedirectView.as_view(url='/')),
]
