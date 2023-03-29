# Generated by Django 4.1.5 on 2023-03-29 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("operations", "0070_alter_operationtask_user_alter_stores_is_site_taken"),
    ]

    operations = [
        migrations.AlterField(
            model_name="operationtask",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="operation_rel",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
