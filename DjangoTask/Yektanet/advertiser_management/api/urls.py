from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('advertiser', views.AdvertiserViewSet, basename='advertiser')
router.register('ad', views.AdViewSet, basename='ad')

urlpatterns = router.urls
