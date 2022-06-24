from rest_framework import viewsets

from . import models, serializers, filters


class BOMViewSet(viewsets.ModelViewSet):

    queryset = models.BOM.objects.all()
    serializer_class = serializers.BOMSerializer
    filterset_class = filters.BOMFilterSet


class BOMMaterialViewSet(viewsets.ModelViewSet):

    queryset = models.BOMMaterial.objects.all()
    serializer_class = serializers.BOMMaterialSerializer
    filterset_class = filters.BOMMaterialFilterSet
