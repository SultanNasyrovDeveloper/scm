from rest_framework import serializers

from . import models


class WarehouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Warehouse
        fields = '__all__'


class WarehouseItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WarehouseItem
        fields = '__all__'
