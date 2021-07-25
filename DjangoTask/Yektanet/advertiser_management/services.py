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


def update_advertisers_views(advertisers: list[Advertiser]):
    for advertiser in advertisers:
        update_advertiser_views(advertiser)


def update_advertiser_views(advertiser: Advertiser):
    for ad in advertiser.ads.all():
        ad.inc_views()
