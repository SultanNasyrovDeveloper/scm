from django.db.models import TextChoices


class PurchaseOrderStatus(TextChoices):

    created = 'created'
    dispatched = 'dispatched'
    delivered = 'delivered'
    revoked = 'revoked'
