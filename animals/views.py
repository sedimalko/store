from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal
from django.core.serializers import serialize

# Create your views here.


def serialized_data(data):
    try:
        return serialize("json", data)
    except Exception as exe:
        return serialize("json", [data])


def get_all_animals(request):
    name = request.GET.get("name")
    if name:
        animal = Animal.objects.all().filter(name=name)
        return HttpResponse(serialized_data(animal))
    animals = Animal.objects.all()
    return HttpResponse(serialized_data(animals))


def get_animal(request, animal_id):
    animal = Animal.objects.get(pk=animal_id)
    return HttpResponse(serialized_data(animal))


def get_all_dogs(requst):
    dogs = Animal.objects.filter(kind="D")
    return HttpResponse(serialized_data(dogs))


def order_animals(request):
    animals = Animal.objects.all().order_by("-age")
    return HttpResponse(serialized_data(animals))


def create_animal(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    kind = request.GET.get("kind")
    image_url = request.GET.get("image_url")
    breed = request.GET.get("breed")
    description = request.GET.get("description")
    animal = Animal(
        name=name,
        description=description,
        age=age,
        kind=kind,
        image_url=image_url,
        breed=breed
    )
    animal.save()
    return HttpResponse(
        f"Animal of kind {animal.kind} with name {animal.name} saved to DB"
    )


def edit_animal(request):
    pass


def delete(request):
    pass
