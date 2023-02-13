# Generated by Django 4.1.5 on 2023-02-13 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("human_resource", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
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
                ("description", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeType",
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
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "Employement Type",
                "verbose_name_plural": "Employment Type",
            },
        ),
        migrations.CreateModel(
            name="Jobs",
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
                ("job_title", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("min_salary", models.CharField(max_length=150)),
                ("max_salary", models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name="employee",
            name="salary",
        ),
        migrations.RemoveField(
            model_name="employee",
            name="skills",
        ),
        migrations.CreateModel(
            name="Skill",
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
                ("created_at", models.DateField(auto_now=True)),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_skills_department_relationship",
                        to="human_resource.department",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_skills_employee_relationship",
                        to="human_resource.employee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Salary",
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
                ("amount", models.CharField(max_length=150)),
                ("reduction", models.CharField(max_length=150)),
                ("paid_date", models.DateField()),
                ("created_at", models.DateField(auto_now=True)),
                (
                    "employee",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_jobs_salary_relationship",
                        to="human_resource.employee",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Job_history",
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
                ("start_date", models.DateField(auto_now=True)),
                ("end_date", models.DateField(auto_now=True)),
                (
                    "department",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_department_relationship",
                        to="human_resource.department",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_jobs_employee_relationship",
                        to="human_resource.employee",
                    ),
                ),
                (
                    "jobs",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hr_jobs_relationship",
                        to="human_resource.jobs",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="employee",
            name="department",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employee_department_relationship",
                to="human_resource.department",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="employment_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employee_department_type_relationship",
                to="human_resource.department",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="title",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employee_job_relationship",
                to="human_resource.jobs",
            ),
        ),
    ]
