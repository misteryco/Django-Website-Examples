from django.urls import path

from LabAuthentication.web.views import index, create_user_and_login, permission_debug, show_profile, ProfileView

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_user_and_login, name='create_user_and_login'),
    path('perms/', permission_debug, name='permission_debug'),
    path('profile/1/', show_profile, name='show_profile'),
    path('profile/2/', ProfileView.as_view(), name='show_profile2'),
]
