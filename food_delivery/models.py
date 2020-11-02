from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    order_fields = models.JSONField()


# todo: complete this validation function for below JSON field
def validate_order(self, value):
    pass


class Order(models.Model):
    # create foreign key so that each order can be referenced to a Restaurant in a many-to-one rls
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # flexible order, requires custom validations depending on restaurant
    order_details = models.JSONField()

