from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('api', views.UserViewSet, basename='users')

urlpatterns = router.urls
