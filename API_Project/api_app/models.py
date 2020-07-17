from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=55)
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField()
