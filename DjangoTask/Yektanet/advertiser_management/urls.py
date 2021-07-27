from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AdvertiserListView.as_view(), name='ads-list'),
    path('click/<slug:pk>', views.ClickAdView.as_view(), name='click-ad-view'),
    path('create-ad', views.CreateAdView.as_view(), name='create-ad'),
    path('create-adviser', views.CreateAdvertiserView.as_view(), name='create-adviser'),
    path('ad/<slug:pk>', views.AdDetailView.as_view(), name='ad-detail'),
    path('api/', include('advertiser_management.api.urls')),
]
