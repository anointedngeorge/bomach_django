# Generated by Django 4.1.5 on 2023-02-14 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0004_alter_gallery_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="data",
            field=models.TextField(default=""),
        ),
    ]
