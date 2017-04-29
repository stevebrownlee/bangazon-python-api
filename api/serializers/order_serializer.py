from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('order', 'product', )


class LineItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', )
        depth = 1


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    line_items = LineItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'url',
            'customer',
            'payment_type',
            'created',
            'processed',
            'line_items',
        )
