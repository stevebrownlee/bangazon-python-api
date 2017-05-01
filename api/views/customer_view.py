import json

from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.core import serializers

from rest_framework import viewsets, generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from api.serializers import *
from api.models import *


class CustomerList(generics.ListCreateAPIView):

    def get_serializer_class(self):
        if not self.request.user.is_superuser:
            return RestrictedCustomerSerializer
        return CustomerSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Customer.objects.all()
        lastname = self.request.query_params.get('last_name', None)
        if lastname is not None:
            queryset = queryset.filter(last_name=lastname)
        return queryset


class CustomerDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('-pk')
    serializer_class = GroupSerializer

