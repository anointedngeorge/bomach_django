# Generated by Django 4.1.5 on 2023-03-07 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authuser", "0008_remove_branchaccessories_image_branch_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="branchaccessories",
            name="assets_type",
            field=models.CharField(
                blank=True, choices=[("d", "sd")], max_length=150, null=True
            ),
        ),
    ]
