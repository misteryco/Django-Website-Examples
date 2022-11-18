from django import forms
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from usersdemos2.auth_app.forms import SignUpForm


# from usersdemos2.auth_app.models import Profile


# Create your views here.
# bGT6jjauMFevy_f

# UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    # Signs the user in, after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


# class SignInForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')


# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInForm()
#     else:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             # print(user)
#             if user:
#                 login(request, user)
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign-in.html', context=context)

class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'
    # success_url = reverse_lazy('index')
