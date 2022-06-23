from rest_framework.viewsets import ModelViewSet

from . import models, serializers, filters


class EnterpriseViewSet(ModelViewSet):

    queryset = models.Enterprise.objects.all()
    serializer_class = serializers.EnterpriseSerializer
    filterset_class = filters.EnterpriseFilterSet


class FactoryViewSet(ModelViewSet):

    queryset = models.Factory.objects.all()
    serializer_class = serializers.FactorySerializer
    filterset_class = filters.FactoryFilterSet
