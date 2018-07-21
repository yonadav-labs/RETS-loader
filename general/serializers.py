from rest_framework import serializers

from general.models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('__all__')
