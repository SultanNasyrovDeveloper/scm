from email.quoprimime import unquote
from django.db import models


class Routing(models.Model):
    """
    Represents full routing of SKU through various workstations (i.e. stages of manufacturing)
    """

    sku = models.ForeignKey(
        'sku.Sku',
        on_delete=models.CASCADE,
        related_name='routing'
    )

class Routing_Node(models.Model):
    """
    Represents an individual routing node of an SKU at a particular manufacturing stage
    """

    order = models.IntegerField(unique=False)

    #in seconds, I suppose? or should we implement enum of uom for cycle time as well?
    cycle_time = models.IntegerField(unique=False) 

    #the time between the end of the current node(manufacturing stage) and the next one
    #in seconds?
    lag_time = models.IntegerField(unique = False) 

    parent = models.ForeignKey(
        'routing.Routing',
        on_delete=models.CASCADE,
        related_name='full_route'
    )