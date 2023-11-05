import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task


def create_pet(name: str, species: str):
    pet = Pet.objects.create(name=name, species=species)
    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(name=name, origin=origin, age=age, description=description, is_magical=is_magical)
    return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    locations = Location.objects.all().order_by("-id")
    return '\n'.join(str(l) for l in locations)


def new_capital():
    city = Location.objects.first()
    city.is_capital = True
    city.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
    city = Location.objects.first()
    city.delete()


def apply_discount():
    cars = Car.objects.all()
    for car in cars:
        discount = sum(int(x) for x in str(car.year)) / 100
        car.price_with_discount = float(car.price) - (float(car.price) * discount)
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)
    return '\n'.join(str(x) for x in tasks)


def complete_odd_tasks():
    tasks = Task.objects.all()
    for task in tasks:
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    decoded_text = ''.join(chr(ord(x) - 3) for x in text)
    tasks_with_matching_title = Task.objects.filter(title=task_title)
    for task in tasks_with_matching_title:
        task.description = decoded_text
        task.save()
