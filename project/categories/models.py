import uuid

from django.db import models
from django.conf import settings

from project.wallets.models import Wallet


class Category(models.Model):
    """A way to categorize and group together Transactions."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(
        Wallet,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="categories",
    )
    name = models.CharField(max_length=25)
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="categories"
    )
    date_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.full_path

    @property
    def full_path(self):
        paths = [self.name]

        p = self.parent
        while p is not None:
            paths.append(p.name)
            p = p.parent

        return " -> ".join(paths[::-1])
