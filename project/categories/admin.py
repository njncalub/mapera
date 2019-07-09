from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "full_path", "created_by", "date_created", "is_active")
    list_filter = ("date_created", "is_active")
