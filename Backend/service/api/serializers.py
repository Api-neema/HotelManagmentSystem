from rest_framework import serializers

from service.models import service

class serviceSerializer(serializers.ModelSerializer):

    class Meta():
        model = service
        fields = ('id','serviceName','description', 'fees', 'type', 'image')
