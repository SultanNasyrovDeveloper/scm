from django_filters import rest_framework as filters

from . import models


class PurchaseOrderFilterSet(filters.FilterSet):

    class Meta:
        model = models.PurchaseOrder
        fields = '__all__'


class PurchaseItemFilterSet(filters.FilterSet):

    class Meta:
        model = models.PurchaseItem
        fields = '__all__'


class VendorFilterSet(filters.FilterSet):

    class Meta:
        model = models.Vendor
        fields = '__all__'
