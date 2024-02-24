from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# TODO: CHeck username and


class CustomMinLengthValidator(MinLengthValidator):
    message = 'Username must be at least 3 characters long.'


def validate_username(value):
    is_valid = all(ch.isalnum() or ch == "_" for ch in value)
    if not is_valid:
        raise ValidationError("Username must contain only letters, digits, and underscores!")


class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=(CustomMinLengthValidator(3), validate_username),
        null=False,
        blank=False,
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(21)],
        help_text="Age requirement: 21 years and above."
    )
    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
