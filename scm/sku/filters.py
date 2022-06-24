from django_filters import rest_framework as filters

from . import models


class SKUCategoryFilterSet(filters.FilterSet):

    class Meta:
        model = models.SKUCategory
        fields = '__all__'


class SKUFilterSet(filters.FilterSet):

    class Meta:
        model = models.SKU
        fields = '__all__'
