# Generated by Django 4.1.5 on 2023-04-12 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("operations", "0083_quotesmodel_comment_quotesmodel_ns"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quotesmodel",
            name="comment",
            field=models.TextField(default=True),
        ),
    ]
