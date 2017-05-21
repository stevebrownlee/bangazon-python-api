from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'first_name',
            'last_name',
            'email',
            'groups',
        )
        extra_kwargs = {
            'is_admin': {'write_only': True},
            'password': {'write_only': True},
        }
        read_only_fields = (
            'is_staff',
            'is_superuser',
            'is_active',
            'date_joined',
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class RestrictedCustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        fields = (
            'id',
            'url',
            'user',
        )


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        fields = (
          'id',
          'url',
          'user',
          'created',
          'street_address',
          'city',
          'state',
          'zipcode',
        )


class CustomerPanelSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = Customer
        fields = (
          'id',
          'url',
          'created',
          'first_name',
          'last_name',
          'street_address',
          'city',
          'state',
          'zipcode',
          'products',
        )
