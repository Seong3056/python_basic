# Generated by Django 5.0.1 on 2024-01-26 05:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Commnet",
            new_name="Comment",
        ),
    ]
