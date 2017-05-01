from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api.views import *

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^$', api_root),
    url(r'^customers/$',
        CustomerList.as_view(),
        name="customer-list"),
    url(r'^customers/(?P<pk>[0-9]+)/$',
        CustomerDetail.as_view(),
        name="customer-detail"),
    url(r'^paymenttypes/$',
        PaymentTypeViewSet.as_view({'get': 'list', 'post': 'create'}),
        name="paymenttype-list"),
    url(r'^paymenttypes/(?P<pk>[0-9]+)/$',
        PaymentTypeViewSet.as_view({'get': 'retrieve'}),
        name="paymenttype-detail"),
    url(r'^producttypes/$',
        ProductTypeViewSet.as_view({'get': 'list', 'post': 'create'}),
        name="producttype-list"),
    url(r'^producttypes/(?P<pk>[0-9]+)/$',
        ProductTypeViewSet.as_view({'get': 'retrieve'}),
        name="producttype-detail"),
    url(r'^products/$',
        ProductViewSet.as_view({'get': 'list', 'post': 'create'}),
        name="product-list"),
    url(r'^products/(?P<pk>[0-9]+)/$',
        ProductViewSet.as_view({'get': 'retrieve'}),
        name="product-detail"),
    url(r'^orders/$',
        OrderViewSet.as_view({'get': 'list', 'post': 'create'}),
        name="order-list"),
    url(r'^orders/(?P<pk>[0-9]+)/$',
        OrderViewSet.as_view({'get': 'retrieve'}),
        name="order-detail"),
    url(r'^users/$',
        UserViewSet.as_view({'get': 'list', 'post': 'create'}),
        name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$',
        UserViewSet.as_view({'get': 'retrieve'}),
        name="user-detail"),
    url(r'^groups/$',
        GroupViewSet.as_view({'get': 'list'}),
        name="group-list"),
    url(r'^groups/(?P<pk>[0-9]+)/$',
        GroupViewSet.as_view({'get': 'retrieve'}),
        name="group-detail"),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]

