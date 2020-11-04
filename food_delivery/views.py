from django.shortcuts import render
from django.http import HttpResponse

from . import services


def index(request):
    return HttpResponse("Hello, world. You're at the food delivery index.")


def get_restaurant(request, *args, **kwargs):
    restaurant_id = kwargs.get("restaurant_id")
    return HttpResponse(services.get_restaurant_by_id(restaurant_id))


def get_all_restaurants(request, *args, **kwargs):
    return HttpResponse(services.get_restaurants())