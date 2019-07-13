from django.contrib import admin

from .models import Category, StandardCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["name", "wallet__name"]
    raw_id_fields = ("parent", "wallet", "created_by")
    list_display = (
        "name",
        "kind",
        "wallet",
        "full_path",
        "created_by",
        "date_created",
        "is_active",
    )
    list_filter = ("kind", "date_created", "is_active")


@admin.register(StandardCategory)
class StandardCategoryAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    raw_id_fields = ("parent", "created_by")
    list_display = ("name", "kind", "full_path", "created_by", "date_created")
    list_filter = ("kind", "date_created")
