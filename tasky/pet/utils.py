from faker import Faker

from tasky.pet.models import Animal


def generate_url(animal_id: int) -> str:
    base_url = "http://127.0.0.1:8000/"
    return f"{base_url}/pet/{animal_id}"


def generate_animal_description(
    faker: Faker,
    animals: list,
) -> str:
    animal_type = faker.random_element(
        elements=animals,
    )

    characteristic1 = faker.random_element(
        elements=("big", "small", "fast", "slow", "colorful", "striped")
    )
    characteristic2 = faker.random_element(
        elements=("long", "short", "fluffy", "scaly", "feathered", "slimy")
    )

    description = f"The beautiful {animal_type}, {characteristic1} pet with {characteristic2} wool."
    return description
