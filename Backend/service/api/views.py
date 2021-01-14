from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from service.models import service
from service.api.serializers import serviceSerializer

class servicesApi(viewsets.ModelViewSet):
    queryset = service.objects.all()
    serializer_class = serviceSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
