# Generated by Django 4.1.5 on 2023-03-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("operations", "0065_remove_stores_site"),
    ]

    operations = [
        migrations.AddField(
            model_name="operationsite",
            name="site_code",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
