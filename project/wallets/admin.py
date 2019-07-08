from django.contrib import admin


from .models import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "initial_balance",
        "currency",
        "created_by",
        "date_created",
        "is_active",
    )
    list_filter = ("is_active",)
