from rest_framework import serializers

from . import models


class WorkStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.WorkStation
        fields = '__all__'


class RoutingStationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.RoutingStation
        fields = '__all__'


class SKURoutingSerializer(serializers.ModelSerializer):

    stations = RoutingStationSerializer(many=True, read_only=True)

    class Meta:
        model = models.SKURouting
        fields = '__all__'



