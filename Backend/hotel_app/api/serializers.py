from rest_framework import serializers

from hotel_app.models import hotel

class  hotelSerializer(serializers.ModelSerializer):

    class Meta():
        model = hotel
        fields = ('hotelName','hotelAddress', 'singleRooms', 'doubleRooms', 'tripleRooms')
