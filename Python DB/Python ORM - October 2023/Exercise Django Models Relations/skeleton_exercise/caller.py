import os
import django
from django.db.models import Avg
from datetime import timedelta, date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Artist, Song, Product, Review, DrivingLicense, Driver, Owner, Car, Registration


def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by('id')
    result = []
    for author in authors:
        written_books = [str(x) for x in author.books.all()]
        if not written_books:
            continue
        result.append(f"{author.name} has written - {', '.join(written_books)}!")
    return "\n".join(result)


def delete_all_authors_without_books():
    Author.objects.filter(books__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by("-id")


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    products = Product.objects.filter(name=product_name)
    return products.aggregate(Avg("reviews__rating"))['reviews__rating__avg']


def get_reviews_with_high_ratings(threshold: int):
    reviews = Review.objects.filter(rating__gte=threshold)
    return reviews


def get_products_with_no_reviews():
    products = Product.objects.filter(reviews__isnull=True).order_by("-name")
    return products


def delete_products_without_reviews():
    products = Product.objects.filter(reviews__isnull=True)
    products.delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all().order_by("-license_number")
    result = []

    for l in licenses:
        license_number = l.license_number
        expiration_date = l.issue_date + timedelta(days=365)
        result.append(f"License with id: {license_number} expires on {expiration_date}!")

    return "\n".join(result)


def get_drivers_with_expired_licenses(due_date):
    expiration_cutoff_date = due_date - timedelta(days=365)

    expired_drivers = Driver.objects.filter(drivinglicense__issue_date__gt=expiration_cutoff_date)

    return expired_drivers


def register_car_by_owner(owner: object):
    first_registration = Registration.objects.filter(car__isnull=True).first()
    first_car = Car.objects.filter(registration__isnull=True).first()

    first_car.owner = owner
    first_car.registration = first_registration
    first_car.save()

    first_registration.registration_date = date.today()
    first_registration.car = first_car

    first_registration.save()

    return (f"Successfully registered {first_car.model} to {owner.name} "
            f"with registration number {first_registration.registration_number}.")


