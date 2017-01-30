from django.db import models
from . import customer, paymenttype


class Order(models.Model):
    customer = models.ForeignKey(
      customer.Customer, 
      on_delete=models.CASCADE,
      related_name='orders'
    )
    payment_type = models.ForeignKey(
      paymenttype.PaymentType, 
      on_delete=models.DO_NOTHING,
      blank=True,
      null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    processed = models.NullBooleanField()

