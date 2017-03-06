from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
from api.serializers import *
from api.models import *
from django.core import serializers
import json


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Customers to be viewed or edited.
    """
    queryset = customer_model.Customer.objects.all().order_by('-created')
    serializer_class = customer_serializer.CustomerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return customer_serializer.RestrictedUserSerializer
        return customer_serializer.UserSerializer 

class LoginView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class=login_serializer.LoginSerializer
    queryset=User.objects.all()

    error_messages = {
        'invalid': "Invalid username or password",
        'disabled': "Sorry, this account is suspended",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }

    def post(self,request):
        req_body = json.loads(request.body.decode())
        username = req_body['username']
        password = req_body['password']
        print(username, password)
        user = authenticate(username=username, password=password)

        success = False
        if user is not None:
            if user.is_active:
                login(request, user)
                success=True

        data = json.dumps({"success":success})
        return HttpResponse(data, content_type='application/json')


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = customer_serializer.GroupSerializer
