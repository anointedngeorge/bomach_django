# Generated by Django 4.1.5 on 2023-02-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0008_alter_customer_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="code",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
