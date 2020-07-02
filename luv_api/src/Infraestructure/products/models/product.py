from django.db import models


class Product(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField()
