import uuid

from django.db import models
from django.conf import settings


class Wallet(models.Model):
    """An abstract or physical location where money can be stored."""

    # TODO(njncalub): Add all the other currencies or use a different model.
    CURRENCY_PHP = "PHP"
    CURRENCY_USD = "USD"
    CURRENCY_CHOICES = [
        (CURRENCY_PHP, f"{CURRENCY_PHP} - Philippine Peso"),
        (CURRENCY_USD, f"{CURRENCY_USD} - United States Dollar"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=25)
    # We'll be using integers to save floating point numbers (e.g. 1482.80 becomes 1482000).
    initial_balance = models.IntegerField(default=0)
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, default=CURRENCY_PHP
    )
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wallets"
    )
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.currency})"
