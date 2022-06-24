from django.db import models

from .enums import POStatus


class PurchaseOrder(models.Model):
    """
    Represents an instance of a purhase order for a particular SKU or a set of SKUs
    """

    status = models.CharField(
        max_length=50,
        choices=POStatus.choices,
        default=POStatus.created
    )
    created_datetime = models.DateTimeField(auto_now=True)
    estimated_delivery_datetime = models.DateTimeField()
    actual_delivery_datetime = models.DateTimeField()
    vendor = models.ForeignKey(
        'supply.Vendor',
        related_name='purchase_orders',
        null=False,
        on_delete=models.DO_NOTHING
    )


class PurchaseItem(models.Model):
    """
    Represents an item of a purchase order
    """

    purchase_order = models.ForeignKey(
        'supply.PurchaseOrder',
        on_delete=models.CASCADE,
        related_name='items'
    )
    sku = models.ForeignKey(
        'sku.SKU',
        on_delete=models.DO_NOTHING
    )
    purchased_quantity = models.DecimalField()
    delivered_quantity = models.DecimalField()


class Vendor(models.Model):
    """
    Represents a vendor/supplier of raw/packing materials and/or services
    """

    name = models.CharField(
        max_length=255,
        default = ''
    )
    default_transit_time_ms = models.IntegerField(null=False)
