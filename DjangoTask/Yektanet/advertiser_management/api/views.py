from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .serializers import AdvertiserSerializer, AdSerializer
from advertiser_management.models import Advertiser, Ad


class StandardResultSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 2


class AdvertiserViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertiserSerializer
    queryset = Advertiser.objects.all()
    permission_classes = [AllowAny, ]
    pagination_class = StandardResultSetPagination


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.filter(approved=True)
    pagination_class = StandardResultSetPagination
