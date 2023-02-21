# Generated by Django 4.1.5 on 2023-02-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0008_remove_servicecategory_service_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="gallery",
            name="data",
        ),
        migrations.RemoveField(
            model_name="gallery",
            name="filename",
        ),
        migrations.RemoveField(
            model_name="gallery",
            name="size",
        ),
        migrations.RemoveField(
            model_name="gallery",
            name="type",
        ),
        migrations.AddField(
            model_name="gallery",
            name="model_id",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="gallery",
            name="model_name",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
