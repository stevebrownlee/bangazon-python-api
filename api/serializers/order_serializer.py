from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = orderproduct_model.OrderProduct
        fields = ('order', 'product', )


class LineItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = orderproduct_model.OrderProduct
        fields = ('order', 'product', )
        depth = 1


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    line_items = LineItemSerializer(many=True, read_only=True)

    class Meta:
        model = order_model.Order
        fields = ('id', 'customer', 'payment_type', 'created', 'processed', 'line_items',)
