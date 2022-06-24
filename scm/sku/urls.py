from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('skus', views.SKUViewSet)
router.register('categories', views.SKUCategoryViewSet)
urlpatterns = router.urls