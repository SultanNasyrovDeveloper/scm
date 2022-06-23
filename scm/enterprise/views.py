from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class EnterpriseViewSet(ModelViewSet):

    queryset = models.Enterprise.objects.all()
    serializer_class = serializers.EnterpriseSerializer


class FactoryViewSet(ModelViewSet):

    queryset = models.Factory.objects.all()
    serializer_class = serializers.FactorySerializer
