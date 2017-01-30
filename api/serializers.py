from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import product, paymenttype, customer, order, orderproduct, producttype

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = producttype.ProductType
        fields = ('id', 'title',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product.Product
        fields = ('id', 'customer', 'title', 'description', 'price', 'quantity')


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = product.Product
        fields = ('id', 'customer', 'title', 'description', 'price', 'quantity')


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = orderproduct.OrderProduct
        fields = ('order', 'product', )


class LineItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = orderproduct.OrderProduct
        fields = ('order', 'product', )
        depth=2


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    line_items = LineItemSerializer(many=True, read_only=True)

    class Meta:
        model = order.Order
        fields = ('id', 'customer', 'payment_type', 'created', 'processed', 'line_items',)
        depth=0


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = customer.Customer
        fields = ('id', 
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
        depth=0


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paymenttype.PaymentType
        fields = ('id', 'customer', 'account_number', 'provider')
