from .models import Restaurant
from django.db import models


def get_restaurants() -> models.QuerySet:
    return Restaurant.objects.all()


def get_restaurant_by_id(_id: int) -> models.QuerySet:
    return Restaurant.objects.get(id=_id)

