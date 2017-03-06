from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import *


class LoginSerializer(serializers.ModelSerializer):
     class Meta:
         model=User
         fields=('email','password') 
