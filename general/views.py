from django.db.models import Q

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route

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

    def retrieve(self, request, pk, format=None):
        entity = self.get_object()
        serializer = FullPropertySerializer(entity)
        return Response(serializer.data)

    @list_route(methods=['POST'])
    def search(self, request):
        page = int(request.GET.get('page', 1))
        page_size = int(request.GET.get('page_size', 50))
        start = (page - 1) * page_size
        end = page * page_size
        filters = request.data

        if 'keyword' in filters:
            value = filters['keyword']
            filters = ['display_address', 'city', 'state', 'state_prov_fullname', 'zip_code', 
                       'mls_id', 'street_name', 'street_number', 'street_type', 'display_mlsnumber']
            q = Q()
            for ii in filters:
                q |= Q(**{ii+'__icontains': value})
        else:
            q = Q()
            for key, value in filters.items():
                if not '__' in key:
                    key = key + '__icontains'
                q &= Q(**{key: value})

        qs = Property.objects.filter(q)[start:end]
        serializer = self.get_serializer(qs, many=True)

        return Response({
            'count': Property.objects.filter(q).count(),
            'results': serializer.data
        })


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

