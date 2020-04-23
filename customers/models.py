from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, commit=True):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address.'))
        if not first_name:
            raise ValueError(_('Users must have a first name.'))
        if not last_name:
            raise ValueError(_('Users must have a last name.'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('email address'), max_length=255, unique=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=50)
    # password and last_login fields supplied by AbstractBaseUser

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )
    # is_superuser, groups, user_permissions fields are provided by PermissionsMixin

    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')

    def get_full_name(self):
        """Returns the first_name plus the last_name, with a space in between."""
        return f'{self.first_name} {self.last_name}'.strip()

    def __str__(self):
        return f'{self.get_full_name()} <{self.email}>'
