from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/enterprise/', include('scm.enterprise.urls')),
    path('api/v1/sku/', include('scm.sku.urls')),
    path('api/v1/supply/', include('scm.supply.urls')),
    path('api/v1/routing/', include('scm.routing.urls')),
    path('api/v1/bom/', include('scm.bom.urls')),
]
