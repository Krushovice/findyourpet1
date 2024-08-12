from tasky.pet.models import Animal


def generate_url(animal_id: int) -> str:
    base_url = "http://127.0.0.1:8000/"
    return f"{base_url}/pet/{animal_id}"
