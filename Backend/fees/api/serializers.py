from rest_framework import serializers

from fees.models import conductedFees

class conductedFeesSerializer(serializers.ModelSerializer):

    class Meta():
        model = conductedFees
        fields = ('user','room', 'totalFees','adminFees')
        lookup_field = 'user'
        extra_kwargs = {
            'url': {'lookup_field': 'user'}
        }
