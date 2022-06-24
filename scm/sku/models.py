from tkinter import CASCADE
from unicodedata import category
from django.db import models
from django.utils.translation import gettext_lazy as _

class Sku(models.Model):
    """
    Represents instance of stock-keeping unit (SKU)
    """

    class Uom(models.TextChoices):
        """
        Represents enum for units of measurement (UoM) of SKU
        """

        PCS = 'pcs', _('Pieces')
        KG = 'kg', _('Kilograms')
        L = 'l', _('Liters')
        M = 'm', _('Meters')
        M2 = 'sqm', _('Square meters')
        M3 = 'cum', _('Cubic meters')


    name = models.CharField(max_length=255)
    unit_of_measurement = models.CharField(
        max_length=3,
        choices=Uom.choices,
        default=Uom.PCS)

class Sku_Category(models.Model):
    """
    Represents the category of SKU
    """
    name = models.CharField(max_length=255)
    sku = models.ForeignKey(
        'sku.Sku',
        related_name='category'
    )