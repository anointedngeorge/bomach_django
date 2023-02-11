# Generated by Django 4.1.5 on 2023-02-11 21:32

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0004_alter_employee_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="country",
            field=django_countries.fields.CountryField(default="---", max_length=2),
        ),
    ]
