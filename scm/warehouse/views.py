from rest_framework import viewsets

from . import models, serializers, filters


class WarehouseViewSet(viewsets.ModelViewSet):

    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer
    filterset_class = filters.WarehouseFilterSet


class WarehouseItemViewSet(viewsets.ModelViewSet):

    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseItemsSerializer
    filterset_class = filters.WarehouseFilterSet

