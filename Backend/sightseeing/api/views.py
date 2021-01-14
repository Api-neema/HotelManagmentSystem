from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from sightseeing.models import query
from sightseeing.api.serializers import querySerializer

class queryApi(viewsets.ModelViewSet):
    queryset =query.objects.all()
    serializer_class = querySerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
