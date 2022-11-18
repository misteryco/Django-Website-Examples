from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from usersdemos2.auth_app.forms import SignUpForm

UserModel = get_user_model()


# Register your models here.
@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    list_filter = ()
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login']
    add_form = SignUpForm
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'password1', 'password2'), }),
        (None, {'classes': ('wide',),
                'fields': ('first_name', 'last_name', 'age'), }),
    )
