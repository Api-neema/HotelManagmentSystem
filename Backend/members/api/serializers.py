from rest_framework import serializers

from members.models import Users

class UsersSerializer(serializers.ModelSerializer):

    class Meta():
        model = Users
        fields = ('id','firstName', 'lastName', 'password', 'mobileNumber',
        'gender', 'email', 'dateOfBirth', 'type','service','card')
