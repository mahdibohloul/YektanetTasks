import itertools

from django.db import models

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
    result = {}
    objs = model.objects.filter(ad=ad).order_by('-created_on')
    groups = itertools.groupby(objs, lambda x: x.created_on.replace(minute=0, second=0, microsecond=0))
    for group, matches in groups:
        result[group] = sum(1 for _ in matches)
    return result
