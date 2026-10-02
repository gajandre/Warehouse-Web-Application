from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Add_WarehouseItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    Price = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



