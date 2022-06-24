from django_filters import rest_framework as filters

from . import models


class BOMFilterSet(filters.FilterSet):

    class Meta:
        model = models.BOM
        fields = '__all__'


class BOMMaterialFilterSet(filters.FilterSet):

    class Meta:
        model = models.BOMMaterial
        fields = '__all__'
