from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import CustomUserForm
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserForm
    model = CustomUser
    list_display = ('email', 'username', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)
