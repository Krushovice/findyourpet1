from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=25, default="Dog")
    age = models.IntegerField()
    owner_first_name = models.CharField(max_length=50)
    owner_last_name = models.CharField(max_length=50)
    owner_phone_number = PhoneNumberField(region="RU")
    special_signs = models.CharField(max_length=100)
