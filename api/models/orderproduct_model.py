from django.db import models
from .product_model import Product
from .order_model import Order


class OrderProduct(models.Model):
    order = models.ForeignKey(
      Order,
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
    product = models.ForeignKey(
      Product,
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
