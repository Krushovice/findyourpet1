from django.core.management.base import BaseCommand, CommandError

import pandas as pd
from tasky.pet.utils import generate_url


class Command(BaseCommand):
    help = "Generate 500 unique urls and save it as .xml file"

    def handle(self, *args, **options):
        data = []

        for i in range(1, 501):
            url = generate_url(animal_id=i)
            animal_id = i
            data.append([animal_id, url])

        df = pd.DataFrame(data, columns=["id", "url"])

        # сохраняем файл
        df.to_excel("static/links.xlsx", index=False)
