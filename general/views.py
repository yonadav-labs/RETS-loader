from django.shortcuts import render

from rest_framework import viewsets

from general.models import *


class PropertyViewSet(viewsets.ModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all()

