from rest_framework import serializers

from room.models import room

class roomSerializer(serializers.ModelSerializer):

    class Meta():
        model = room
        fields = ('id','number', 'number', 'type', 'fees')
