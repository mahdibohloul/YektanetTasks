from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import RedirectView, CreateView
from .models import Advertiser, Ad
from .services import get_ad_by_pk, update_advertisers_views
from .forms import CreateAdForm


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


class CreateAdView(CreateView):
    form_class = CreateAdForm
    template_name = 'advertiser_management/create_ad.html'
    success_url = '/'
