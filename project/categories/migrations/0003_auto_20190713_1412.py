# Generated by Django 2.2.3 on 2019-07-13 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("categories", "0002_category_wallet"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="kind",
            field=models.CharField(
                choices=[("DR", "INCOME"), ("CR", "EXPENSE")],
                default="CR",
                max_length=2,
            ),
        ),
        migrations.CreateModel(
            name="StandardCategory",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "kind",
                    models.CharField(
                        choices=[("DR", "INCOME"), ("CR", "EXPENSE")],
                        default="CR",
                        max_length=2,
                    ),
                ),
                ("name", models.CharField(max_length=25)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="standard_categories",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="children",
                        to="categories.StandardCategory",
                    ),
                ),
            ],
            options={"verbose_name_plural": "standard categories"},
        ),
    ]
