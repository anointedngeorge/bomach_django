# Generated by Django 4.1.5 on 2023-03-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("operations", "0019_operationcontract_contract_value_currency_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="operationproject",
            name="budget_currency",
        ),
        migrations.AlterField(
            model_name="operationproject",
            name="budget",
            field=models.CharField(max_length=150, null=True),
        ),
    ]
