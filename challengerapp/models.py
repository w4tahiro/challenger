from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self.name