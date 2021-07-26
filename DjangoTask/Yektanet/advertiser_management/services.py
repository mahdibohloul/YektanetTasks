from django.db.models import Q, F, Count, Avg
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


def __prepare_num_apart_hour(model, ad: Ad):
    model_name = "advertiser_management_" + model.__name__.lower()
    result = model.objects.raw(
        f"SELECT 1 as id, COUNT(id) as \"count\", DATE_TRUNC('hour', {model_name}.\"created_on\" AT TIME ZONE 'UTC') AS \"created_date\" FROM {model_name} WHERE {model_name}.\"ad_id\" = {ad.id} GROUP BY DATE_TRUNC('hour', {model_name}.\"created_on\" AT TIME ZONE 'UTC') ORDER BY \"created_date\" DESC ")

    return result


def __get_created_times(model, ad):
    created_times = model.objects.filter(ad=ad).annotate(created_time=Trunc('created_on', 'hour')).distinct(
        'created_time').values_list('created_time').order_by('created_time')
    return created_times

