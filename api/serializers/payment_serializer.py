from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('id', 'url', 'customer', 'account_number', 'provider')
