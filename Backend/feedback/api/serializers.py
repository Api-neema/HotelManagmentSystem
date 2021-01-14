from rest_framework import serializers

from feedback.models import feedback

class feedbackSerializer(serializers.ModelSerializer):

    class Meta():
        model = feedback
        fields = ('feedback','email', 'userName')
