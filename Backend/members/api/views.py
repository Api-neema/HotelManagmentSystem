from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from members.models import Users
from payment.models import Payment

from members.api.serializers import UsersSerializer
from payment.api.serializers import PaymentSerializer

class UsersApi(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination

    @action(detail=False, methods=['post'])
    def loginCheck(self, request):
        users = list(self.get_queryset())
        for user in users:
            print (type(user))
            if user.email==request.data['email'] and user.password == request.data['password']:
                try:
                    serializer = UsersSerializer(user )
                    print (serializer)
                    return Response(serializer.data)
                except:
                    return Response(status.Http404)
        return Response({'status':'Wrong login details'})
