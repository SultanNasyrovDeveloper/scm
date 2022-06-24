from rest_framework import serializers

from . import models


class SKUCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SKUCategory
        fields = '__all__'


class SKUSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SKU
        fields = '__all__'
