from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .serializers import AdvertiserSerializer, AdSerializer
from advertiser_management.models import Advertiser, Ad
from advertiser_management.services import update_ads_views, update_advertisers_views, update_advertiser_views


class StandardResultSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 2


class AdvertiserViewSet(viewsets.ModelViewSet):
    serializer_class = AdvertiserSerializer
    queryset = Advertiser.objects.all()
    permission_classes = [AllowAny, ]
    pagination_class = StandardResultSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        update_advertisers_views(queryset, request.ip_addr)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        advertiser = self.get_object()
        update_advertiser_views(advertiser, request.ip_addr)
        return super().retrieve(request, *args, **kwargs)


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    queryset = Ad.objects.filter(approved=True)
    pagination_class = StandardResultSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        update_ads_views(queryset, request.ip_addr)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        ad = self.get_object()
        ad.inc_views(request.ip_addr)
        return super().retrieve(request, *args, **kwargs)
