import random
import pandas as pd
from django.core.management.base import BaseCommand

from tasky.pet.models import Animal, Url
from tasky.pet.utils import generate_animal_description

from faker import Faker

faker = Faker("ru_RU")

animals = ["Cat", "Dog", "Bird", "Fish", "Snake", "Spider"]


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Read links from Excel file
        links_df = pd.read_excel("static/links.xlsx")
        template = "+7-9{}{}-{}{}{}-{}{}{}{}"
        for index, row in links_df.iterrows():
            link = row["url"]  # assuming the column name is 'link'

            # Create an animal
            animal = Animal(
                name=faker.first_name(),
                kind=random.choice(animals),
                age=faker.pyint(min_value=1, max_value=20),
                owner_first_name=faker.first_name(),
                owner_last_name=faker.last_name(),
                owner_phone_number=template.format(
                    *[random.randint(0, 9) for _ in range(10)]
                ),
                special_signs=generate_animal_description(faker, animals),
            )
            animal.save()

            # Create a Url object with the link
            url = Url(url=link, pet=animal)
            url.save()
