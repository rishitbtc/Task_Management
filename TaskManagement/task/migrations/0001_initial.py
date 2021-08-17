# Generated by Django 3.2.5 on 2021-07-27 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(blank=True, max_length=50, null=True)),
                ("description", djrichtextfield.models.RichTextField()),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("Lower", "Lower"),
                            ("Medium", "Medium"),
                            ("High", "High"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "To-do"),
                            ("2", "In-progress"),
                            ("3", "Done"),
                            ("4", "Declined"),
                            ("5", "Ready For Testing"),
                            ("6", "Code Review"),
                            ("7", "Testing in-progress"),
                        ],
                        max_length=30,
                    ),
                ),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                (
                    "tasktype",
                    models.CharField(
                        choices=[
                            ("1", "Bug"),
                            ("2", "Improvement"),
                            ("3", "New Feature"),
                            ("4", "Story"),
                            ("5", "Task"),
                            ("6", "Epic"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "assigned_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_task",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="task.task",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sprint",
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("1", "Planning"),
                            ("2", "Active"),
                            ("3", "Accepted"),
                            ("4", "Closed"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="task.task"
                    ),
                ),
            ],
        ),
    ]
