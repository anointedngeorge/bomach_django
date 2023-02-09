# Generated by Django 4.1.5 on 2023-02-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("realestate", "0021_alter_realestatepayment_total_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="realestatepayment",
            name="third_party_email",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="realestatepayment",
            name="third_party_name",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="realestatepayment",
            name="third_party_phone",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
