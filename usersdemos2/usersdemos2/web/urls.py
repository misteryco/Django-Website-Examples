from django.urls import path

from usersdemos2.web.views import UsersListView


urlpatterns = [
    path('', UsersListView.as_view(), name='index'),
]
