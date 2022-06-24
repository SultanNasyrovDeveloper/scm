from rest_framework import viewsets

from . import models, serializers, filters


class WorkStationViewSet(viewsets.ModelViewSet):

    queryset = models.WorkStation.objects.all()
    serializer_class = serializers.WorkStationSerializer
    filterset_class = filters.WorkStationFilterSet


class SKURoutingViewSet(viewsets.ModelViewSet):

    queryset = models.SKURouting.objects.all()
    serializer_class = serializers.SKURoutingSerializer
    filterset_class = filters.SKURoutingFilterSet


class RoutingStationViewSet(viewsets.ModelViewSet):

    queryset = models.RoutingStation.objects.all()
    serializer_class = serializers.RoutingStationSerializer
    filterset_class = filters.RoutingStationFilterSet

