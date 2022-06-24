from django_filters import rest_framework as filters

from . import models


class EnterpriseFilterSet(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Enterprise
        fields = ('name', )


class FactoryFilterSet(filters.FilterSet):

    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = models.Factory
        fields = ('name', 'enterprise')