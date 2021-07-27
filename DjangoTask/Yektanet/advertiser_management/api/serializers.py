from rest_framework import serializers

from advertiser_management.models import Ad, Advertiser
from advertiser_management.services import num_of_ad_views_apart_hour, num_of_ad_clicks_apart_hour


class AdSerializer(serializers.ModelSerializer):
    approved = serializers.BooleanField(read_only=True)

    class Meta:
        model = Ad
        fields = ['advertiser', 'title', 'image', 'link', 'approved', 'ctr']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['views_report'] = num_of_ad_views_apart_hour(instance)
        data['clicks_report'] = num_of_ad_clicks_apart_hour(instance)
        return data


class AdvertiserSerializer(serializers.ModelSerializer):
    ads = serializers.SerializerMethodField('get_ads')

    class Meta:
        model = Advertiser
        fields = ['name', 'ads']

    def get_ads(self, instance):
        ads_queryset = Ad.objects.filter(advertiser=instance, approved=True)
        serializer = AdSerializer(read_only=True, instance=ads_queryset, many=True)
        return serializer.data
