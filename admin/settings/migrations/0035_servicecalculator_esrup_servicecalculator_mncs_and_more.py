# Generated by Django 4.1.5 on 2023-04-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("settings", "0034_alter_servicecalculator_function"),
    ]

    operations = [
        migrations.AddField(
            model_name="servicecalculator",
            name="esrup",
            field=models.IntegerField(
                default=0, verbose_name="Extra Sitting Room Unit Price"
            ),
        ),
        migrations.AddField(
            model_name="servicecalculator",
            name="mncs",
            field=models.IntegerField(
                default=0, verbose_name="Maximum number of category sitting room"
            ),
        ),
        migrations.AddField(
            model_name="servicecalculator",
            name="ns",
            field=models.IntegerField(default=0, verbose_name="Number of sitting room"),
        ),
    ]
