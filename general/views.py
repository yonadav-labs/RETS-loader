from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from general.models import *
from general.serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    pagination_class = StandardResultsSetPagination
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

