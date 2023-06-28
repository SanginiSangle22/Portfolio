# Generated by Django 4.2.2 on 2023-06-17 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_service"),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio",
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
                (
                    "project_title",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "project_link",
                    models.CharField(blank=True, max_length=1000, null=True),
                ),
                (
                    "img",
                    models.ImageField(
                        default="images/project.png", null=True, upload_to="images"
                    ),
                ),
            ],
        ),
    ]