from django.contrib import admin


from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "get_timestamp",
        "wallet",
        "get_debit",
        "get_credit",
        "is_committed",
    )
    list_filter = ("on", "date_created", "is_committed", "is_active")

    def get_timestamp(self, obj):
        return obj.timestamp

    get_timestamp.short_description = "Timestamp"
    get_timestamp.admin_order_field = "transaction__on"

    def get_debit(self, obj):
        return f"{obj.str_debit}"

    get_debit.short_description = "Debit"
    get_debit.admin_order_field = "transaction__debited"

    def get_credit(self, obj):
        return f"{obj.str_credit}"

    get_credit.short_description = "Credit"
    get_credit.admin_order_field = "transaction__credited"
