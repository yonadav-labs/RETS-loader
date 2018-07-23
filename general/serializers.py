from rest_framework import serializers

from general.models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('__all__')


class PropertyAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAttribute
        fields = ('__all__')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('__all__')


class MlsAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlsAgent
        fields = ('__all__')


class MlsOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MlsOffice
        fields = ('__all__')


class OpenHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenHouse
        fields = ('__all__')


class PropertyRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyRoom
        fields = ('__all__')
