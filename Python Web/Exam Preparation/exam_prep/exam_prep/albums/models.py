from django.core.validators import MinValueValidator
from django.db import models

from exam_prep.profiles.models import Profile


class Album(models.Model):
    GENRE_CHOICES = [
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ('R&B Music', 'R&B Music'),
        ('Rock Music', 'Rock Music'),
        ('Country Music', 'Country Music'),
        ('Dance Music', 'Dance Music'),
        ('Hip Hop Music', 'Hip Hop Music'),
        ('Other', 'Other'),
    ]
    name = models.CharField(
        max_length=30,
        unique=True,
        null=False,
        blank=False
    )
    artist_name = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    genre = models.CharField(
        max_length=30,
        choices=GENRE_CHOICES,
        null=False,
        blank=False
    )
    description = models.TextField()
    image_url = models.URLField(
        null=False,
        blank=False
    )
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='albums', editable=False)
