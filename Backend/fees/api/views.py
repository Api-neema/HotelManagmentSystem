from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

from fees.models import conductedFees
from fees.api.serializers import conductedFeesSerializer

class conductedFeesApi(viewsets.ModelViewSet):
    lookup_field = 'user'
    queryset = conductedFees.objects.all()
    serializer_class = conductedFeesSerializer

    def get_object(self):
        try:
            print(self.request.data)
            return conductedFees.objects.get(user=self.request.data['user'],room=self.request.data['room'] )
        except conductedFees.DoesNotExist:
            raise Http404


    def update(self, request, *args, **kwargs):
        partial = True # Here I change partial to True
        instance = self.get_object()
        # print(request.data)
        # print(instance.data)
        request.data['totalFees'] = str(int(request.data['totalFees']) +int( instance.totalFees))
        # print(instance)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

    pagination_class = PageNumberPagination
