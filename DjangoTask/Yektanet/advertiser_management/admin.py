from django.contrib import admin, messages
from .models import Advertiser, Ad, Click, View


class CommonInlineForm(admin.StackedInline):
    readonly_fields = ['id', 'created_on']
    extra = 0

    def has_add_permission(self, request, obj):
        return False


class ClickInline(CommonInlineForm):
    model = Click


class ViewInLine(CommonInlineForm):
    model = View


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'advertiser', 'approved', 'total_clicks', 'total_views']
    list_filter = ['approved', 'advertiser__name']
    search_fields = ['title', 'advertiser__name']
    inlines = [ClickInline, ViewInLine]
    actions = ['mark_as_approved', ]

    fieldsets = (
        ('General info', {
            'fields': ['advertiser', 'title', 'approved']
        }),
        ('Media info', {
            'fields': ['image', 'link']
        })
    )

    def mark_as_approved(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(
            request, f'{updated} ads mark as approved', messages.SUCCESS
        )


class AdTabular(admin.TabularInline):
    model = Ad
    extra = 0


@admin.register(Advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    search_fields = ['name', 'ads__title']
    list_display = ['name', 'get_total_clicks', 'get_total_views']
    inlines = [AdTabular, ]
