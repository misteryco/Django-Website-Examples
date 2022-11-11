from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.views import generic

from LabAuthentication.web.decorators import allow_groups


@login_required(login_url='/admin/login/')
def show_profile(request):
    return HttpResponse(f'You are {request.user.username}')


class ProfileView(LoginRequiredMixin, generic.View):
    def get(self, request):
        return HttpResponse(f'You are {self.request.user}')


@allow_groups(groups=['Users'])
def index(request):
    usr_message3 = f"{authenticate(username='jorda', password='12345')}"
    usr_message4 = f"{authenticate(username='misterdai', password='12345')}"
    # new_user = User.objects.create_user(
    #     username='misterdi',
    #     password='12345',
    #     first_name='misterdi'
    # )
    usr_message = '' if request.user.is_authenticated else ' not '
    usr_message2 = f'{request.user}'
    return HttpResponse(
        f' The user is {usr_message} is_authenticated.; '
        f'<p>{usr_message2}; '
        f'<p>{usr_message3}; '
        f'<p>{usr_message4}')


def create_user_and_login(request):
    message_1 = f'{request.user}'
    the_user = User.objects.create_user(
        username='misterdi1',
        password='12345',
        first_name='misterdi1'
    )
    # create session, attach user to request
    login(request, the_user)

    return HttpResponse(
        f' {message_1}'
    )


def permission_debug(request):
    usernames = {'jorda', 'misterdi', 'some', 'misterdi1'}
    users = User.objects.filter(username__in=usernames)
    permissions_to_check = ('auth.add_user', 'auth.change_user', 'auth.delete_user', 'auth.view_user',)
    result = ''
    for user in users:
        for perm in permissions_to_check:
            result += f"<p>{user}: {perm}: {user.has_perm(perm)}"
            result += f"<p>{30 * ' - '}"
    return HttpResponse(
        f'It works:'
        f'{result}')
    #
    #     f'<p> {[f"<p> User: {user.username}:  {user.user_permissions}" for user in users]}'
    #     f'<p> {30 * "-"} '
    #     f'<p> {[f"<p> User: {user.username}:  {user.has_perms(permissions_to_check)}" for user in users]}'
    #     f'<p> {30 * "-"} '
    #     f'<p> {[f"<p> User: {user.username}:  {user.has_perms(permissions_to_check)}" for user in users]}')
    # f'<p> {[f"<p> User: {user.username}:  {user.has_perms(permissions_to_check)}" for user in users]}')
