# Generated by Django 4.2.16 on 2024-10-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("property", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="listings",
            name="image",
            field=models.ImageField(default="", upload_to=""),
            preserve_default=False,
        ),
    ]