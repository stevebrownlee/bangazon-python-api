from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'customers': reverse('customer-list', request=request, format=format),
        'groups': reverse('group-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'producttypes': reverse('producttype-list', request=request, format=format),
        'paymenttypes': reverse('paymenttype-list', request=request, format=format),
    })