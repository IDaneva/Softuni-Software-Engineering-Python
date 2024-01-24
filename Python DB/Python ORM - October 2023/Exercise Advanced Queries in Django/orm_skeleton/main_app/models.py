from datetime import timezone, timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q, Count, Avg, F


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type: str):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price, max_price):
        return self.filter(Q(price__lte=max_price) & Q(price__gte=min_price))

    def with_bedrooms(self, bedrooms_count):
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        return self.values('location').annotate(
            location_count=Count('location')
        ).order_by('-location_count', 'id')[:2]


class RealEstateListing(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('House', 'House'),
        ('Flat', 'Flat'),
        ('Villa', 'Villa'),
        ('Cottage', 'Cottage'),
        ('Studio', 'Studio'),
    ]

    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    objects = RealEstateListingManager()


def rating_validation(value):
    if value < 0 or value > 10:
        raise ValidationError("The rating must be between 0.0 and 10.0")


def year_validation(value):
    if value < 1990 or value > 2023:
        raise ValidationError("The release year must be between 1990 and 2023")


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre):
        return self.filter(genre=genre)

    def recently_released_games(self, year):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        return self.all().order_by("-rating").first()

    def lowest_rated_game(self):
        return self.all().order_by("-rating").last()

    def average_rating(self):
        average = self.aggregate(average_result=Avg('rating'))["average_result"]
        return f"{average:.1f}"


class VideoGame(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'RPG'),
        ('Adventure', 'Adventure'),
        ('Sports', 'Sports'),
        ('Strategy', 'Strategy'),
    ]

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES)
    release_year = models.PositiveIntegerField(validators=[year_validation])
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[rating_validation])

    def __str__(self):
        return self.title

    objects = VideoGameManager()


class BillingInfo(models.Model):
    address = models.CharField(max_length=200)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    billing_info = models.OneToOneField(BillingInfo, on_delete=models.CASCADE)

    @classmethod
    def get_invoices_with_prefix(cls, prefix: str):
        return cls.objects.select_related('billing_info').filter(invoice_number__startswith=prefix)

    @classmethod
    def get_invoices_sorted_by_number(cls):
        return cls.objects.select_related('billing_info').order_by('invoice_number')

    @classmethod
    def get_invoice_with_billing_info(cls, invoice_number: str) -> object:
        return cls.objects.select_related('billing_info').get(invoice_number=invoice_number)


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technologies_used = models.ManyToManyField(Technology, related_name='projects')

    def get_programmers_with_technologies(self):
        return self.programmers.prefetch_related('projects__technologies_used')


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    projects = models.ManyToManyField(Project, related_name='programmers')

    def get_projects_with_technologies(self):
        return self.projects.prefetch_related('technologies_used')


class Task(models.Model):
    PRIORITIES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=PRIORITIES)
    is_completed = models.BooleanField(default=False)
    creation_date = models.DateField()
    completion_date = models.DateField()

    @classmethod
    def overdue_high_priority_tasks(cls):
        return cls.objects.filter(
            Q(priority="High") & Q(is_completed=False) & Q(completion_date__gt=F('creation_date'))
        )

    @classmethod
    def completed_mid_priority_tasks(cls):
        # return cls.objects.filter(priority="Medium", is_completed=True)
        return cls.objects.filter(
            Q(priority="Medium") & Q(is_completed=True)
        )

    @classmethod
    def search_tasks(cls, query: str):
        return cls.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    def recent_completed_tasks(self, days: int):
        return Task.objects.filter(
            Q(is_completed=True) & Q(completion_date__gte=self.creation_date - timedelta(days=days))
        )


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    difficulty_level = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    repetitions = models.PositiveIntegerField()

    @classmethod
    def get_long_and_hard_exercises(cls):
        return cls.objects.filter(
            duration_minutes__gt=30,
            difficulty_level__gte=10,
        )

    @classmethod
    def get_short_and_easy_exercises(cls):
        return cls.objects.filter(
            duration_minutes__lt=15,
            difficulty_level__lt=5,
        )

    @classmethod
    def get_exercises_within_duration(cls, min_duration: int, max_duration: int):
        return cls.objects.filter(
            duration_minutes__range=(min_duration, max_duration)
        )

    @classmethod
    def get_exercises_with_difficulty_and_repetitions(cls, min_difficulty: int, min_repetitions: int):
        return cls.objects.filter(
            difficulty_level__gte=min_difficulty,
            repetitions__gte=min_repetitions
        )


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)