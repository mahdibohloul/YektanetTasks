from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdListView.as_view(), name='ads-list'),
    path('click/<slug:pk>', views.ClickAdView.as_view(), name='click-ad-view'),
    path('create-ad', views.CreateAdView.as_view(), name='create-ad'),
    path('create-adviser', views.CreateAdvertiserView.as_view(), name='create-adviser'),
]
