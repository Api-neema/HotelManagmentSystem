from rest_framework import serializers

from review.models import review

class reviewSerializer(serializers.ModelSerializer):

    class Meta():
        model = review
        fields = ('description','rating', 'userName')
