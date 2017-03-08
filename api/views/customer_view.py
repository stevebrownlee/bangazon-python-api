from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.http import HttpResponse
from django.core import serializers
import json

from api.serializers import *
from api.models import *


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = customer_model.Customer.objects.all().order_by('-created')
    serializer_class = customer_serializer.CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return customer_serializer.RestrictedUserSerializer
        return customer_serializer.UserSerializer 

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = customer_serializer.GroupSerializer
