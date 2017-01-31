from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class RestrictedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')

class RestrictedCustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = customer_model.Customer
        fields = (
            'id', 
            'url', 
            'first_name', 
            'last_name', 
        )

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = customer_model.Customer
        fields = (
          'id', 
          'url', 
          'user', 
          'created', 
          'first_name', 
          'last_name', 
          'street_address', 
          'city', 
          'state', 
          'zipcode',
          'products'
        )
