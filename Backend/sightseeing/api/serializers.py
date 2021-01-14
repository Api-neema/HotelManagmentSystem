from rest_framework import serializers

from sightseeing.models import query

class querySerializer(serializers.ModelSerializer):

    class Meta():
        model = query
        fields = ('query','email', 'userName','user')
