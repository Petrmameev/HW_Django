# Generated by Django 4.2 on 2023-05-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("phones", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="phone",
            name="slug",
            field=models.SlugField(),
        ),
    ]
