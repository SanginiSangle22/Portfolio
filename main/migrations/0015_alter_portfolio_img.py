# Generated by Django 4.2.2 on 2024-02-29 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_profile_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.CharField(max_length=1000, null=True, verbose_name='img: (1920 x 1080)'),
        ),
    ]