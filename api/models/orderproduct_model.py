from django.db import models
from .order_model import Order
from .product_model import Product


class OrderProduct(models.Model):
    """The OrderProduct model represents the relationship between an order
    and a product

        Fields:
            order - Order
            product - Product
    """
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
