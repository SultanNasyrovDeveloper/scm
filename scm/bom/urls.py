from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('boms', views.BOMViewSet)
router.register('bom_materials', views.BOMMaterialViewSet)
urlpatterns = router.urls
