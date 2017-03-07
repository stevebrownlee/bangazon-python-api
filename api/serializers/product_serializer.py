from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *
from . import customer_serializer


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = producttype_model.ProductType
        fields = ('id', 'title',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # customer = customer_serializer.RestrictedCustomerSerializer(read_only=True)

    class Meta:
        model = product_model.Product
        fields = (
            'id', 
            'url', 
            'customer', 
            'producttype', 
            'title', 
            'description', 
            'price', 
            'quantity',
        )
        depth=1
