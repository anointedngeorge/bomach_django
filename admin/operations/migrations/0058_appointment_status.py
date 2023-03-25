# Generated by Django 4.1.5 on 2023-03-25 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("operations", "0057_alter_appointment_designation"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("pending", "Pending")],
                default="pending",
                max_length=150,
                null=True,
            ),
        ),
    ]
