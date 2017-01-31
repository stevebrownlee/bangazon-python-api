from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from api.models import *


class OrderProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = orderproduct_model.OrderProduct.objects.all()
    serializer_class = order_serializer.OrderProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = order_model.Order.objects.all()
    serializer_class = order_serializer.OrderSerializer
