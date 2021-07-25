from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import RedirectView

from .models import Advertiser
from .services import get_ad_by_pk, update_advertisers_views


def ad_list(request):
    advertisers = Advertiser.objects.all()
    update_advertisers_views(advertisers)

    context = {
        'advertisers': advertisers
    }
    return render(request, 'advertiser_management/ads.html', context=context)


class ClickAdView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        ad_pk = kwargs['pk']
        ad = get_ad_by_pk(ad_pk)
        if ad is None:
            messages.error(self.request, 'Could not find any Ad with this specific identifier')
            return reverse('ads-list')
        ad.inc_clicks()
        return ad.link
