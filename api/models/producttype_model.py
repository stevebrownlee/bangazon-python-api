from django.db import models


class ProductType(models.Model):
    """The ProductType model represents a classification of a Product

        Fields:
            title - CharField
    """
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title
