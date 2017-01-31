from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paymenttype_model.PaymentType
        fields = ('id', 'customer', 'account_number', 'provider')
