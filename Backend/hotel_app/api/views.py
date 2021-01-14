from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from hotel_app.models import hotel
from hotel_app.api.serializers import hotelSerializer

class hotelApi(viewsets.ModelViewSet):
    queryset = hotel.objects.all()
    serializer_class = hotelSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
