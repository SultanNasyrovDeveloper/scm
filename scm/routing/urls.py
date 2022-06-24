from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('workstations', views.WorkStationViewSet)
router.register('routings', views.SKURoutingViewSet)
router.register('stations', views.RoutingStationViewSet)
urlpatterns = router.urls