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
    update_ads_views(advertiser.get_approved_ads(), ip_addr)


def update_ads_views(ads: list[Ad], ip_addr):
    for ad in ads:
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


# TODO complete this part
def ctr_per_hour(ad: Ad):
    view_count = View.objects.filter(ad=1).annotate(
        time=Trunc('created_on', 'hour', output_field=DateTimeField())).values(
        'time').annotate(count=Count('id'))

    click_count = Click.objects.filter(ad=1).annotate(
        time=Trunc('created_on', 'hour', output_field=DateTimeField())).values(
        'time').annotate(count=Count('id'))


def view_to_click_avg(ad: Ad):
    last_click = ad.clicks.order_by('-created_on')[0]
    last_view = ad.views.filter(ip=last_click.ip).order_by('-created_on')[0]
