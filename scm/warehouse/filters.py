from django_filters import rest_framework as filters

from . import models


class WarehouseFilterSet(filters.FilterSet):

    class Meta:
        model = models.Warehouse
        fields = '__all__'


class WarehouseItemFilterSet(filters.FilterSet):

    class Meta:
        model = models.WarehouseItem
        fields = '__all__'
