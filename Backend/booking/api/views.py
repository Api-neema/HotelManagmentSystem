from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from booking.models import booking
from booking.api.serializers import bookingSerializer

class bookingApi(viewsets.ModelViewSet):
    queryset =booking.objects.all()
    serializer_class = bookingSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
