from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from room.models import room
from room.api.serializers import roomSerializer

class roomApi(viewsets.ModelViewSet):
    queryset = room.objects.all()
    serializer_class = roomSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
