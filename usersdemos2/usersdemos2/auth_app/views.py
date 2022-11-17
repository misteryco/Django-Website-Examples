from django import forms
from django.contrib.auth import forms as auth_forms, login, get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

# Create your views here.
# bGT6jjauMFevy_f

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        # fields = ('first_name', 'last_name', 'username')
        fields = '__all__'
        field_classes = {'username': auth_forms.UsernameField}

    # auto defining username from first and last name
    def save(self, commit=True):
        user = super().save(commit=commit)
        user.username = user.first_name + '-' + user.last_name
        if commit:
            user.save()
        return user


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


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
