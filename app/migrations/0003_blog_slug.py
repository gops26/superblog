# Generated by Django 4.2.20 on 2025-03-27 03:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_blog_cover_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
