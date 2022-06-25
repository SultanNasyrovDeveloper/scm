from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('warehouses', views.WarehouseViewSet)
router.register('warehouse_items', views.WarehouseItemViewSet)

urlpatterns = router.urls
