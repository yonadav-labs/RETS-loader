from django.shortcuts import render

from rest_framework import viewsets

from general.models import *
from general.serializers import *


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()


class PropertyAttributeViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyAttributeSerializer
    queryset = PropertyAttribute.objects.all()


class PhotoViewSet(viewsets.ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class MlsAgentViewSet(viewsets.ModelViewSet):
    serializer_class = MlsAgentSerializer
    queryset = MlsAgent.objects.all()


class MlsOfficeViewSet(viewsets.ModelViewSet):
    serializer_class = MlsOfficeSerializer
    queryset = MlsOffice.objects.all()


class OpenHouseViewSet(viewsets.ModelViewSet):
    serializer_class = OpenHouseSerializer
    queryset = OpenHouse.objects.all()


class PropertyRoomViewSet(viewsets.ModelViewSet):
    serializer_class = PropertyRoomSerializer
    queryset = PropertyRoom.objects.all()

