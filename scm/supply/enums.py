from django.db.models import TextChoices

class POStatus(TextChoices):
    created = 'created'
    dispatched = 'dispatched'
    delivered = 'delivered'