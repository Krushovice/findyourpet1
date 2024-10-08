# Generated by Django 5.1 on 2024-08-12 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Url",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(unique=True)),
                (
                    "pet",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="animal_url",
                        to="pet.animal",
                    ),
                ),
            ],
        ),
    ]
