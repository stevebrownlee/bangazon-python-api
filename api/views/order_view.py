from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from api.models import *


class OrderProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = Order.objects.all().order_by("-created")
    serializer_class = OrderSerializer
