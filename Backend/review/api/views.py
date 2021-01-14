from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from review.models import review
from review.api.serializers import reviewSerializer

class reviewApi(viewsets.ModelViewSet):
    queryset =review.objects.all()
    serializer_class = reviewSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
