# Generated by Django 4.2.2 on 2023-06-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_portfolio"),
    ]

    operations = [
        migrations.CreateModel(
            name="Portfolio_description",
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
                ("desc", models.TextField(max_length=5000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="portfolio",
            name="img",
            field=models.ImageField(
                default="images/project.png",
                null=True,
                upload_to="images",
                verbose_name="img: (1920 x 1080)",
            ),
        ),
    ]
