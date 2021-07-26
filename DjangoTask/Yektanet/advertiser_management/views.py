from django.contrib import messages
from django.urls import reverse
from django.views.generic import RedirectView, CreateView, TemplateView, DetailView

from .forms import CreateAdForm, CreateAdvertiserForm
from .models import Advertiser, Ad
from .services import get_ad_by_pk, update_advertisers_views, num_of_ad_views_apart_hour, num_of_ad_clicks_apart_hour


class AdListView(TemplateView):
    template_name = 'advertiser_management/ads.html'

    def get_context_data(self, **kwargs):
        advertisers = Advertiser.objects.all()
        print(self.request.ip_addr)
        update_advertisers_views(advertisers, self.request.ip_addr)
        context = {
            'advertisers': advertisers
        }

        return context


class ClickAdView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        ad_pk = kwargs['pk']
        ad = get_ad_by_pk(ad_pk)
        if ad is None:
            messages.error(self.request, 'Could not find any Ad with this specific identifier')
            return reverse('ads-list')
        ad.inc_clicks(self.request.ip_addr)
        return ad.link


class CreateAdView(CreateView):
    form_class = CreateAdForm
    template_name = 'advertiser_management/create_ad.html'
    success_url = '/'


class CreateAdvertiserView(CreateView):
    form_class = CreateAdvertiserForm
    template_name = 'advertiser_management/create_advertiser.html'
    success_url = '/'


class AdDetailView(DetailView):
    model = Ad
    template_name = 'advertiser_management/ad_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.get_object()
        views = num_of_ad_views_apart_hour(ad)
        clicks = num_of_ad_clicks_apart_hour(ad)
        context['views'] = views
        context['clicks'] = clicks
        return context
