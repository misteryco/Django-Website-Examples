from django.urls import path

from UsersDemos.web.views import UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='index'),
]
