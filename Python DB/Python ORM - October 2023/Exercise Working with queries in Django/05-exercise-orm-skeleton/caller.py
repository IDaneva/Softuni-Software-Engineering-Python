import os
import django
from django.db.models import Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, Laptop


def show_highest_rated_art():
    highest_art = ArtworkGallery.objects.all().order_by('-rating').first()
    return f"{highest_art.art_name} is the highest-rated art with a {highest_art.rating} rating!"


def bulk_create_arts(first_art, second_art):
    ArtworkGallery.objects.bulk_create([first_art, second_art])


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    most_expensive_laptop = Laptop.objects.all().order_by("-price", "id").first()
    return f"{most_expensive_laptop.brand} is the most expensive laptop available for {most_expensive_laptop.price}$!"


def bulk_create_laptops(*args):
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage():
    Laptop.objects.filter(Q(brand='Asus') | Q(brand='Lenovo')).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(Q(brand='Apple') | Q(brand='Dell')| Q(brand='Acer')).update(memory=16)


def update_operation_systems():
    laptops = Laptop.objects.all()
    for laptop in laptops:
        if laptop.brand == "Asus":
            laptop.operation_system = "Windows"
            laptop.save()
        elif laptop.brand == "Apple":
            laptop.operation_system = "MacOS"
            laptop.save()
        elif laptop.brand == "Dell" or laptop.brand == "Acer":
            laptop.operation_system = "Linux"
            laptop.save()
        elif laptop.brand == "Lenovo":
            laptop.operation_system = "Chrome OS"
            laptop.save()


def delete_inexpencive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()

