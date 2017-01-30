from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import product, paymenttype, customer


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product.Product
        fields = ('id', 'customer', 'title', 'description', 'price', 'quantity')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = customer.Customer
        fields = ('id', 'user', 'created', 'first_name', 'last_name', 'street_address', 'city', 'state', 'zipcode')


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paymenttype.PaymentType
        fields = ('id', 'customer', 'account_number', 'provider')