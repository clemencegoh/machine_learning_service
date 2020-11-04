from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('restaurants', views.get_all_restaurants),
    path('restaurants/<int:restaurant_id>', views.get_restaurant),
]