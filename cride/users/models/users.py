"""User  model."""

# Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """
    User model.

    Extends from Django's AbstractUser Class and changes his default USERNAME_FIELD
    option, from 'username' to 'email' attribute, adding besides some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +9999999999 up to 15 digits allowed.'
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        blank=True
    )

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text=(
            'Helps to easily distinguish clients from staff in queries. '
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to True when the user has verified his email address.'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS= ['username', 'first_name', 'last_name']

    def __str__(self):
        """Returns username."""
        return self.username

    def get_short_name(self):
        """Returns username."""
        return self.username