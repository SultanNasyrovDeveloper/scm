from django.db import models


class Enterprise(models.Model):
    """
    Represents enterprise instance.
    """

    name = models.CharField(max_length=1000)


class Factory(models.Model):
    """
    Represents factory instance.
    """

    enterprise = models.ForeignKey(
        'enterprise.Enterprise',
        on_delete=models.CASCADE,
        related_name='factories'
    )
    name = models.CharField(max_length=1000)
