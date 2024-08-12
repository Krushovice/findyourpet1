import random

from django.core.management.base import BaseCommand, CommandError
from tasky.pet.models import Animal
from faker import Faker

faker = Faker("ru_RU")

animals = ["Cat", "Dog", "Bird", "Fish", "Snake", "Spider", "Other"]


class GenericExel(BaseCommand):
    help = "Generate 500 unique pets and save it as .xml file"

    def handle(self, *args, **options):
        for _ in range(500):
            animal = Animal(
                name=faker.name(),
                kind=random.choice(animals),
                owner_first_name=faker.first_name(),
                owner_last_name=faker.last_name(),
                owner_phone_number=faker.phone_number(),
                special_signs=faker.text(max_nb_chars=100),
            )
            animal.save()
