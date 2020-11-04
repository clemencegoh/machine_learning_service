from django.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)

    objects = models.Manager()


# todo: complete this validation function for below JSON field
def validate_order(self, value):
    pass


# General field for ordering items flexibly for different restaurants
class OrderItem(models.Model):
    item_name = models.CharField(max_length=100)
    item_quantity = models.IntegerField()


class OrderDetails(models.Model):
    order_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, editable=False)
    order_done = models.BooleanField(default=False)
    order_items = models.ManyToManyField(OrderItem)  # expect many items

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

