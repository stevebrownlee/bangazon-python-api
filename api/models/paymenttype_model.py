from django.db import models
from .customer_model import Customer


class PaymentType(models.Model):
    customer = models.ForeignKey(
      'Customer', 
      on_delete=models.CASCADE,
      related_name="payment_types",
      related_query_name="payment_type",
    )
    account_number = models.CharField(max_length=25)
    provider = models.CharField(max_length=25)

