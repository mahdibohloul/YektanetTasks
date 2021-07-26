from .models import Ad, Advertiser


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
