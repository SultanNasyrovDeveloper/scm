from django_filters import rest_framework as filters

from . import models


class WorkStationFilterSet(filters.FilterSet):

    class Meta:
        model = models.WorkStation
        fields = '__all__'


class SKURoutingFilterSet(filters.FilterSet):

    class Meta:
        model = models.SKURouting
        fields = '__all__'


class RoutingStationFilterSet(filters.FilterSet):

    class Meta:
        model = models.RoutingStation
        fields = '__all__'
