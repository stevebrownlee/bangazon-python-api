from django.db import models


class Discount(models.Model):
    title = models.CharField(max_length=25)
