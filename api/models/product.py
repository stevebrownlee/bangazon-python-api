from django.db import models
from .customer import Customer
from .producttype import ProductType


class Product(models.Model):
    customer = models.ForeignKey(
      Customer, 
      on_delete=models.CASCADE,
      related_name='products'
    )
    producttype = models.ForeignKey(
      ProductType, 
      on_delete=models.CASCADE,
      related_name='products'
    )
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    quantity = models.IntegerField()

