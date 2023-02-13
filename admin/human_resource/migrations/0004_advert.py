# Generated by Django 4.1.5 on 2023-02-13 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("human_resource", "0003_designation_alter_job_history_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Advert",
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
                ("name", models.CharField(max_length=150)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("description", models.TextField()),
                ("is_hired", models.BooleanField(default=False)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_advert_user_relationship",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_advert_department_relationship",
                        to="human_resource.department",
                    ),
                ),
                (
                    "job_position",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_advert_position_relationship",
                        to="human_resource.jobs",
                    ),
                ),
            ],
            options={
                "verbose_name": "Advert",
                "verbose_name_plural": "Job Advert",
            },
        ),
    ]
