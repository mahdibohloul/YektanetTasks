from django.db import models
from django.db.models import Count, DateTimeField
from django.db.models.functions import Trunc

from .models import Ad, Advertiser, View, Click


def get_ad_by_pk(pk):
    try:
        return Ad.objects.get(pk=pk)
    except Ad.DoesNotExist:
        return None


def get_advertiser_by_pk(pk):
    try:
        return Advertiser.objects.get(pk=pk)
    except Advertiser.DoesNotExist:
        return None


def update_advertisers_views(advertisers: list[Advertiser], ip_addr):
    for advertiser in advertisers:
        update_advertiser_views(advertiser, ip_addr)


def update_advertiser_views(advertiser: Advertiser, ip_addr):
    for ad in advertiser.get_approved_ads():
        ad.inc_views(ip_addr)


def num_of_ad_views_apart_hour(ad: Ad):
    return __prepare_num_apart_hour(View, ad)


def num_of_ad_clicks_apart_hour(ad: Ad):
    return __prepare_num_apart_hour(Click, ad)


def __prepare_num_apart_hour(model: models, ad: Ad):
    result = model.objects.filter(ad=ad).annotate(
        created_date=Trunc('created_on', 'hour', output_field=DateTimeField())).values('created_date').annotate(
        count=Count('id')).order_by('-created_date')
    return result
