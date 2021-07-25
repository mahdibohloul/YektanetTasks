from django.contrib import admin
from .models import Advertiser, Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'clicks', 'views', 'advertiser']
    readonly_fields = ['clicks', 'views']
    search_fields = ['title', 'advertiser__name']
    ordering = ['-clicks', ]


class AdTabular(admin.TabularInline):
    model = Ad
    readonly_fields = ['views', 'clicks']


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ads__title']
    list_display = ['name', 'clicks', 'views']
    readonly_fields = ['clicks', 'views']
    inlines = [AdTabular, ]
    ordering = ['-clicks', ]
