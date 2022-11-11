from django import forms
from django.contrib.auth import forms as auth_forms, login, get_user_model
from django.contrib.auth import views as auth_views
# from django.contrib.auth.models import UserManager
from django.urls import reverse_lazy
from django.views import generic

from UsersDemos.auth_app.models import Profile

# UserManager

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'first_name', 'last_name', 'password1', 'password2', 'age')
        field_classes = {'username': auth_forms.UsernameField}

    # Save with data in profile
    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            age=self.cleaned_data['age'],
            user=user,
        )
        if commit:
            profile.save()

    # # Save with empty profile
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #     profile = Profile(
    #         user=user,
    #     )
    #     if commit:
    #         profile.save()

    # Demo:
    # def save(self, commit=True):
    #     user = super().save(commit=commit)
    #
    #     user.username = user.first_name + '-' + user.last_name
    #
    #     if commit:
    #         user.save()
    #     return user


class SignUpView(generic.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'

# class SignInForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
#
#
# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInForm()
#     else:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # user = authenticate(request, username=username, password=password)
#             user = authenticate(request, **form.cleaned_data)
#             if user:
#                 login(request, user)
#
#     context = {
#         'form': form,
#
#     }
#     return render(request, 'auth/sign-in.html', context=context)
