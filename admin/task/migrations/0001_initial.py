# Generated by Django 4.1.5 on 2023-01-31 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tasks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                ("year", models.DateField(auto_now_add=True, verbose_name="Year")),
            ],
            options={
                "verbose_name": "Tasks",
                "verbose_name_plural": "Tasks",
            },
        ),
    ]
