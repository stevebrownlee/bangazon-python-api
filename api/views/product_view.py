from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from api.models import *


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Product.objects.all().order_by("-price")
    serializer_class = ProductSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ProductTypes to be viewed or edited.
    """
    queryset = ProductType.objects.all().order_by("title")
    serializer_class = ProductTypeSerializer

