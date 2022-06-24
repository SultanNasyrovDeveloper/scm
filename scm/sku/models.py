from django.db import models

from .enums import UnitOfMeasurement


class SKUCategory(models.Model):

    name = models.CharField(max_length=1000)


class SKU(models.Model):
    """
    Stock keeping item.

    Represents any item stored in enterprise stock(warehouse).
    """

    guid = models.CharField(max_length=500)
    category = models.ForeignKey(
        'sku.SKUCategory',
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    is_discrete = models.BooleanField(default=True)
    name = models.CharField(max_length=1000,  default='')
    uom = models.CharField(
        max_length=50,
        choices=UnitOfMeasurement.choices,
        default=UnitOfMeasurement.piece
    )
    price = models.DecimalField(max_digits=8, decimal_places=4, default=0)
    name = models.CharField(max_length=255)

