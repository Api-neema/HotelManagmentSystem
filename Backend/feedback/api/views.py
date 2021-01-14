from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets

from feedback.models import feedback
from feedback.api.serializers import feedbackSerializer

class feedbackApi(viewsets.ModelViewSet):
    queryset =feedback.objects.all()
    serializer_class = feedbackSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
