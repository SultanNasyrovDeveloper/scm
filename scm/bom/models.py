from django.db import models


class Bom(models.Model):
    """
    Represents instance of BOM (bill of materials) for an SKU
    """

    sku = models.ForeignKey(
        'sku.Sku',
        on_delete=models.CASCADE,
        related_name='bom_tree'
    )


class Bom_Node(models.Model):
    """
    Represents a node in the BOM tree of SKU
    """

    level = models.IntegerField(unique=False)
    sku = models.ForeignKey(
        'sku.Sku',
    )
    quantity = models.DecimalField(
        max_digits=3,
        decimal_places=3
    )
    parent = models.ForeignKey(
        'bom.Bom',
        on_delete=models.CASCADE,
        related_name='nodes'
    )
