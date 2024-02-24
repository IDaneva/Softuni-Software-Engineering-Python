from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from djangoProject_exam.user_profile.models import Profile


def validate_car_year(value):
    is_valid = 1999 <= value <= 2030
    if not is_valid:
        raise ValidationError("Year must be between 1999 and 2030!")


class Car(models.Model):
    TYPE_CHOICES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    ]

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        null=False,
        blank=False,
    )
    model = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(1)],
        null=False,
        blank=False,
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[validate_car_year],
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        unique=True,
        error_messages={"unique": "This image URL is already in use! Provide a new one."}
    )
    price = models.DecimalField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1.0)],
        decimal_places=3,
        max_digits=20,
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
