# Generated by Django 4.1.5 on 2023-03-08 06:46

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("authuser", "0022_alter_branchaccessories_value_of_asset"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branchaccessories",
            name="value_of_asset",
            field=djmoney.models.fields.MoneyField(
                decimal_places=2,
                default=Decimal("0"),
                default_currency="NGN",
                max_digits=10,
            ),
        ),
    ]
