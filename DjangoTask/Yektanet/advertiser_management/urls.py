from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ads-list'),
    path('click/<slug:pk>', views.ClickAdView.as_view(), name='click-ad-view'),
    path('create-form', views.CreateAdView.as_view(), name='create-ad'),
]
