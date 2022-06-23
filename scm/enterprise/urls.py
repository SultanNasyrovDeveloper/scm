from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('enterprises', views.EnterpriseViewSet)
router.register('factories', views.FactoryViewSet)

urlpatterns = router.urls
