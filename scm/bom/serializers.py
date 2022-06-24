from rest_framework import serializers

from . import models


class BOMSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BOM
        fields = '__all__'


class BOMMaterialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.BOMMaterial
        fields = '__all__'
