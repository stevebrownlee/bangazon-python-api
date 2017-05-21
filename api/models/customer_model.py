from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """The Customer model is a 1:1 extension of the built-in Django User model

        Fields:
            user - User
            created - DateTime
            street_address - CharField
            city - CharField
            state - CharField
            zipcode - CharField
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)

    class Meta:
        ordering = ('created',)


