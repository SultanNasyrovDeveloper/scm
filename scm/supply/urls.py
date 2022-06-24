from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('purchase_orders', views.PurchaseOrderViewSet)
router.register('vendors', views.VendorViewSet)
urlpatterns = router.urls