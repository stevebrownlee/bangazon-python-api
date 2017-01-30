from django.db import models
from . import product, order


class OrderProduct(models.Model):
    order = models.ForeignKey(
      order.Order, 
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
    product = models.ForeignKey(
      product.Product, 
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
