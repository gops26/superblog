# Generated by Django 4.2.20 on 2025-03-25 10:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="cover_image",
            field=models.ImageField(default="blog_default", upload_to=""),
        ),
    ]
