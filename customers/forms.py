from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Customer


class CustomerCreationForm(forms.ModelForm):
    """
    New Customer Form. Requires password confirmation.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        """Check that the two password entries match."""
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def signup(self, request, user):
        """
        This method is for integrating allauth app with custom user model.
        ModelForm save method does not work with allauth adapter.
        """
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class CustomerChangeForm(forms.ModelForm):
    """
    Update User Form. Doesn't allow changing password in the Admin.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Customer
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_staff')

    def clean_password(self):
        return self.initial["password"]