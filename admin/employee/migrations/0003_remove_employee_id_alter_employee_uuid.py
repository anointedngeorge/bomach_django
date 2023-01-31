# Generated by Django 4.1.5 on 2023-01-31 02:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_employee_uuid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employee",
            name="id",
        ),
        migrations.AlterField(
            model_name="employee",
            name="uuid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
