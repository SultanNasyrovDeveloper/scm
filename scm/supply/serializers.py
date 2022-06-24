from rest_framework import serializers

from . import models


class PurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PurchaseOrder
        fields = '__all__'

class PurchaseItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PurchaseItem
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Vendor
        fields = '__all__'
