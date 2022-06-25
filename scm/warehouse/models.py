from django.db import models


class Warehouse(models.Model):

    factory = models.ForeignKey(
        'enterprise.Factory',
        on_delete=models.CASCADE,
        related_name='warehouses',
        null=True,
        default=None
    )


class WarehouseItem(models.Model):

    warehouse = models.ForeignKey(
        'warehouse.Warehouse',
        on_delete=models.CASCADE,
        related_name='items'
    )
    sku = models.ForeignKey('sku.SKU', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=4)
    reserved_quantity = models.DecimalField(max_digits=10, decimal_places=4)
