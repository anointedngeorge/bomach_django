# Generated by Django 4.1.5 on 2023-03-13 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0017_delete_activities"),
        ("operations", "0035_quotesmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="quotesmodel",
            name="service_category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_category_rel",
                to="settings.servicecategory",
            ),
        ),
        migrations.AlterField(
            model_name="quotesmodel",
            name="service",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="service_rel",
                to="settings.service",
            ),
        ),
    ]
