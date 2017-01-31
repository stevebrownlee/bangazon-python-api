from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from api.models import *


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = product_model.Product.objects.all()
    serializer_class = product_serializer.ProductSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ProductTypes to be viewed or edited.
    """
    queryset = product_model.ProductType.objects.all()
    serializer_class = product_serializer.ProductTypeSerializer

