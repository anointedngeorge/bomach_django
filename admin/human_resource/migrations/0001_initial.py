# Generated by Django 4.1.5 on 2023-02-13 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("address", models.CharField(default="---", max_length=500, null=True)),
                (
                    "phone_number",
                    models.CharField(default="---", max_length=500, null=True),
                ),
                ("date_of_birth", models.DateField(auto_now=True)),
                (
                    "designation",
                    models.CharField(
                        choices=[
                            ("trainee", "Trainee"),
                            ("senior", "Senior"),
                            ("junior", "Junior"),
                            ("teamlead", "Team lead"),
                            ("adhoc", "Adhoc"),
                        ],
                        default="---",
                        max_length=250,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        choices=[
                            ("civilengineer", "Civil Engineer"),
                            ("landsurveyor", "Land Surveyor"),
                            ("marketer", "Marketer"),
                            ("developer", "Developer"),
                            ("secretary", "Secretary"),
                            ("consultants", "Consultants"),
                            ("chiefsecurityofficer", "Chief Security Officer"),
                            ("securityofficer", "Security Officer"),
                            ("technician", "Technician"),
                        ],
                        default="---",
                        max_length=250,
                    ),
                ),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("marketing", "Marketing"),
                            ("sales", "Sales"),
                            ("humanresources", "Human Resources"),
                            ("publicrelations", "Public Relations"),
                            ("research", "Research"),
                            ("financeandAccounts", "finance and Accounts"),
                            ("operations", "Operations"),
                        ],
                        default="---",
                        max_length=250,
                    ),
                ),
                (
                    "employment_type",
                    models.CharField(
                        choices=[
                            ("marketing", "Marketing"),
                            ("sales", "Sales"),
                            ("humanresources", "Human Resources"),
                            ("publicrelations", "Public Relations"),
                            ("research", "Research"),
                            ("financeandAccounts", "finance and Accounts"),
                            ("operations", "Operations"),
                        ],
                        default="---",
                        max_length=250,
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        choices=[
                            ("single", "Single"),
                            ("married", "Married"),
                            ("divorced", "Divorced"),
                        ],
                        default="---",
                        max_length=250,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("others", "Others"),
                        ],
                        default="---",
                        max_length=250,
                    ),
                ),
                (
                    "country",
                    django_countries.fields.CountryField(default="---", max_length=200),
                ),
                ("state", models.CharField(default="---", max_length=50, null=True)),
                ("local_government", models.CharField(default="---", max_length=250)),
                ("town", models.CharField(default="---", max_length=250, null=True)),
                ("about", models.TextField(default="---")),
                ("skills", models.CharField(default="---", max_length=50, null=True)),
                ("salary", models.CharField(default="---", max_length=50, null=True)),
                ("start_date", models.DateField(auto_now=True)),
                ("probation_start_date", models.DateField(auto_now=True)),
                ("probation_end_date", models.DateField(auto_now=True)),
                ("create_at", models.DateField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_employee_relationship",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Employee",
                "verbose_name_plural": "Employee",
            },
        ),
    ]
