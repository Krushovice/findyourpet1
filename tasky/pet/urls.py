from django.urls import path

from . import views

urlpatterns = [
    path("", views.PetIndexView.as_view(), name="pet_index"),
]
