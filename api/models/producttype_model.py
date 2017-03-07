from django.db import models


class ProductType(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title
