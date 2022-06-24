from rest_framework import viewsets

from . import models, filters, serializers


class SKUCategoryViewSet(viewsets.ModelViewSet):

    queryset = models.SKUCategory.objects.all()
    serializer_class = serializers.SKUCategorySerializer
    filterset_class = filters.SKUCategoryFilterSet


class SKUViewSet(viewsets.ModelViewSet):

    queryset = models.SKU.objects.all()
    serializer_class = serializers.SKUSerializer
    filterset_class = filters.SKUFilterSet

