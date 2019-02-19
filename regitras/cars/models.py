from django.db import models


class Licenze(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    car_brand = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
