from rest_framework import viewsets

from . import models, filters, serializers


class PurchaseOrderViewSet(viewsets.ModelViewSet):

    queryset = models.PurchaseOrder.objects.all()
    serializer_class = serializers.PurchaseOrderSerializer
    filterset_class = filters.PurchaseOrderFilterSet


class PurchaseItemViewSet(viewsets.ModelViewSet):
    
    queryset = models.PurchaseItem.objects.all()
    serializer_class = serializers.PurchaseItemSerializer
    filterset_class = filters.PurchaseItemFilterSet


class VendorViewSet(viewsets.ModelViewSet):
    
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    filterset_class = filters.VendorFilterSet
