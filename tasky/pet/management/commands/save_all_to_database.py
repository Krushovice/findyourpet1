import random
import pandas as pd
from django.core.management.base import BaseCommand

from tasky.pet.models import Animal, Url


from faker import Faker

faker = Faker("ru_RU")

animals = ["Cat", "Dog", "Bird", "Fish", "Snake", "Spider", "Other"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Read links from Excel file
        links_df = pd.read_excel("links.xlsx")

        for index, row in links_df.iterrows():
            link = row["link"]  # assuming the column name is 'link'

            # Create an animal
            animal = Animal(
                name=faker.name(),
                kind=random.choice(animals),
                owner_first_name=faker.first_name(),
                owner_last_name=faker.last_name(),
                owner_phone_number=faker.phone_number(),
                special_signs=faker.text(max_nb_chars=100),
            )
            animal.save()

            # Create a Url object with the link
            url = Url(url=link, pet=animal)
            url.save()
