from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomerCreationForm, CustomerChangeForm
from .models import Customer


class UserAdmin(BaseUserAdmin):
    form = CustomerChangeForm
    add_form = CustomerCreationForm

    fieldsets = (
        (None, {
            'fields': ('email', 'password'),
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(Customer, UserAdmin)
