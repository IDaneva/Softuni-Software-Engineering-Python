from django.core.validators import MinValueValidator
from django.db import models

from main_app.validators import check_name_type, check_phone_number


class Customer(models.Model):
    name = models.CharField(max_length=100, validators=[check_name_type])
    age = models.PositiveIntegerField(validators=[MinValueValidator(18, message="Age must be greater than 18")])
    email = models.EmailField(error_messages={'invalid': 'Enter a valid email address'})
    phone_number = models.CharField(max_length=13, validators=[check_phone_number])
    website_url = models.URLField(error_messages={"invalid": "Enter a valid URL"})
