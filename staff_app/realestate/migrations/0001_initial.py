# Generated by Django 4.1.5 on 2023-01-31 10:44

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="RealEstate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=500, null=True)),
                ("total_amount", models.CharField(max_length=500, null=True)),
                ("amount_deposited", models.CharField(max_length=500, null=True)),
                ("unit_price", models.CharField(max_length=500, null=True)),
                ("content", models.CharField(max_length=500, null=True)),
                ("unique_code", models.CharField(max_length=500, null=True)),
                ("is_blocked", models.BooleanField(default=False, null=True)),
                ("is_featured", models.BooleanField(default=False, null=True)),
                ("is_frontend", models.BooleanField(default=False, null=True)),
                ("legal_fee", models.CharField(max_length=500, null=True)),
                ("survey_plan", models.CharField(max_length=500, null=True)),
                ("development_fee", models.CharField(max_length=500, null=True)),
                ("created_at", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "RealEstate",
                "verbose_name_plural": "RealEstate",
            },
        ),
        migrations.CreateModel(
            name="RealEstatePlot",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=uuid.uuid4,
                        editable=False,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=500, null=True)),
                ("price", models.CharField(max_length=500, null=True)),
                ("size", models.CharField(max_length=500, null=True)),
                ("status", models.CharField(max_length=500, null=True)),
                ("content", models.CharField(max_length=500, null=True)),
                ("timer_date", models.DateField(null=True)),
                ("timer", models.TimeField(null=True)),
                ("transactional_code", models.CharField(max_length=500, null=True)),
                ("purchase_code", models.CharField(max_length=500, null=True)),
                ("unique_code", models.CharField(max_length=500, null=True)),
                ("resell_code", models.CharField(max_length=500, null=True)),
                ("payment_id", models.CharField(max_length=500, null=True)),
                ("is_blocked", models.BooleanField(default=False, null=True)),
                ("is_featured", models.BooleanField(default=False, null=True)),
                ("is_frontend", models.BooleanField(default=False, null=True)),
                ("is_sold", models.BooleanField(default=False, null=True)),
                ("created_at", models.DateField(auto_now=True)),
                (
                    "realestate",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="realestate_rel",
                        to="realestate.realestate",
                        verbose_name="Realestate",
                    ),
                ),
            ],
        ),
    ]
