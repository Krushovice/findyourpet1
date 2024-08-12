from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.


class PetIndexView(View):
    def get(self, request, *args, **kwargs):
        animal_photo_url = (
            "https://i.natgeofe.com/n/9135ca87-0115-4a22-8caf-d1bdef97a814/75552.jpg"
        )
        return render(
            request,
            "pets/index.html",
            context={
                "text": "It's the animal which we're find last",
                "url": animal_photo_url,
            },
        )
