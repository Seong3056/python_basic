# Generated by Django 5.0.1 on 2024-02-05 03:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0003_post_like_posts"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="like_posts",
        ),
    ]
