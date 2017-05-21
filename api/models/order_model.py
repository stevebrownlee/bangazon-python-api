from django.db import models
from .customer_model import Customer
from .paymenttype_model import PaymentType


class Order(models.Model):
    """The Order model represents the shopping cart concept in Bangazon

        Fields:
            customer - Customer
            payment_type - PaymentType
            created - DateTime
            processed = NullBoolean
    """
    customer = models.ForeignKey(
      'Customer',
      on_delete=models.CASCADE,
      related_name='orders'
    )
    payment_type = models.ForeignKey(
      'PaymentType',
      on_delete=models.DO_NOTHING,
      blank=True,
      null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    processed = models.NullBooleanField()

    def __str__(self):
      return "{} ({})".format(self.customer, self.created)
