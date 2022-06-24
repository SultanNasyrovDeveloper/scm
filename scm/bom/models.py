from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class BOM(models.Model):
    """
    Bill of materials.
    """
    name = models.CharField(max_length=1000, default='')
    sku = models.ForeignKey(
        'sku.SKU',
        on_delete=models.CASCADE,
        related_name='boms'
    )
    materials = models.ManyToManyField('bom.BOMMaterial', blank=True)


class BOMMaterial(MPTTModel):

    sku = models.ForeignKey(
        'sku.SKU',
        on_delete=models.CASCADE,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    quantity = models.DecimalField(max_digits=8, decimal_places=4)
