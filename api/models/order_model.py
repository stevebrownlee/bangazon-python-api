from django.db import models
from . import customer_model, paymenttype_model


class Order(models.Model):
    customer = models.ForeignKey(
      customer_model.Customer, 
      on_delete=models.CASCADE,
      related_name='orders'
    )
    payment_type = models.ForeignKey(
      paymenttype_model.PaymentType, 
      on_delete=models.DO_NOTHING,
      blank=True,
      null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    processed = models.NullBooleanField()

