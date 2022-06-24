from django.db import models


class WorkStation(models.Model):

    """
    Represents workstation.

    Attributes:
        setup_time: Amount of time in seconds needed to set up station.
        lag_time: Amount of time in seconds spent between sku production.
    """

    factory = models.ForeignKey(
        'enterprise.Factory',
        on_delete=models.CASCADE,
        related_name='workstations'
    )
    name = models.CharField(max_length=1000)
    setup_time = models.IntegerField()


class SKURouting(models.Model):

    sku = models.ForeignKey(
        'sku.SKU',
        on_delete=models.CASCADE,
        related_name='routings'
    )


class RoutingStation(models.Model):

    routing = models.ForeignKey(
        'routing.SKURouting',
        on_delete=models.CASCADE,
        related_name='stations'
    )
    workstation = models.ForeignKey(
        'routing.WorkStation',
        on_delete=models.CASCADE,

    )
    sku = models.ForeignKey(
        'sku.SKU',
        on_delete=models.CASCADE,
    )
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ('order', )
        unique_together = ('routing', 'order')
