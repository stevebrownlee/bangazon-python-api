from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import *
from api.models import *


class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PaymentTypes to be viewed or edited.
    """
    queryset = PaymentType.objects.all().order_by("provider")
    serializer_class = PaymentTypeSerializer
