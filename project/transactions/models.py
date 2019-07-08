import uuid

from django.db import models
from django.conf import settings
from django.utils import timezone

from project.wallets.models import Wallet


class Transaction(models.Model):
    """An activity where money is either credited or debited from a Wallet."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    on = models.DateTimeField("Timestamp", default=timezone.now)
    description = models.TextField()
    credited = models.IntegerField(default=0)
    debited = models.IntegerField(default=0)
    wallet = models.ForeignKey(
        Wallet, on_delete=models.CASCADE, related_name="transactions"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transactions"
    )
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # If it is not yet committed, it should not be added in the final computation.
    is_committed = models.BooleanField(default=False)
    # TODO(njncalub): Add categories/envelopes for the transactions.
    # TODO(njncalub): Add an upload button for the receipts.

    # TODO(njncalub): Move this to a utilities package.
    def floatify(self, value):
        """Converts an integer value to a floating-point value."""
        return value / (10 ** settings.FLOATING_ZEROES)

    # TODO(njncalub): Move this to a utilities package.
    def format_date(self, date):
        """Converts a date to a specified format."""
        return f"{date:%Y-%m-%d %H:%M:%S (%Z)}"

    @property
    def timestamp(self):
        return self.format_date(self.on)

    @property
    def debit(self):
        return self.floatify(self.debited)

    @property
    def credit(self):
        return self.floatify(self.credited)

    @property
    def str_debit(self):
        return f"{self.debit:.3f}"

    @property
    def str_credit(self):
        return f"{self.credit:.3f}"

    @property
    def balance(self):
        return self.floatify(self.debited - self.credited)

    def __str__(self):
        return f"{self.timestamp} [{self.str_debit}|{self.str_credit}]"
