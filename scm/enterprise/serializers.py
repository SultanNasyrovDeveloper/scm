from rest_framework import serializers

from . import models


class EnterpriseSerializer(serializers.ModelSerializer):
    """
    Enterprise model serializer.
    """

    class Meta:
        model = models.Enterprise
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    """
    Factory model serializer.
    """

    class Meta:
        model = models.Factory
        fields = '__all__'
