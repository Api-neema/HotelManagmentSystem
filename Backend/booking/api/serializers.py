from rest_framework import serializers

from booking.models import booking

class bookingSerializer(serializers.ModelSerializer):

    class Meta():
        model = booking
        fields = ('id','user', 'hotelName','roomNumber', 'roomCapacity', 'roomType', 'startDate' ,  'endDate','checkIn','bookingType','service','accepted')
