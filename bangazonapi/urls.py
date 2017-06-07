from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api.views import *

router = routers.DefaultRouter()
router.register(r'users', customer_view.UserViewSet)
router.register(r'groups', customer_view.GroupViewSet)
router.register(r'customers', customer_view.CustomerViewSet)
router.register(r'paymenttypes', payment_view.PaymentTypeViewSet)
router.register(r'products', product_view.ProductViewSet)
router.register(r'orders', order_view.OrderViewSet)
router.register(r'line_items', order_view.OrderProductViewSet)
router.register(r'product_types', product_view.ProductTypeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^register/', register_view.register_user),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
