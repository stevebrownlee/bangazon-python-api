from django.db import models
from . import product_model, order_model


class OrderProduct(models.Model):
    order = models.ForeignKey(
      order_model.Order,
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
    product = models.ForeignKey(
      product_model.Product,
      on_delete=models.DO_NOTHING,
      related_name='line_items',
    )
