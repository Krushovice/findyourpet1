from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from tasky.pet.models import Animal


# Create your views here.


class PetIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "pets/index.html",
            context={
                "text": "It's the animal information which we're find",
            },
        )


class PetShowView(View):
    def get(self, request, *args, **kwargs):
        pet_id = kwargs.get("pk")
        pet = get_object_or_404(Animal, pk=pet_id)
        return render(
            request,
            "pets/show.html",
            context={
                "pet": pet,
            },
        )
