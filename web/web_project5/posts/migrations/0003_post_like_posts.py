# Generated by Django 5.0.1 on 2024-02-05 03:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_hashtag_post_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="like_posts",
            field=models.ManyToManyField(
                blank=True,
                related_name="like_users",
                to="posts.post",
                verbose_name="좋아요 누른 Post 목록",
            ),
        ),
    ]
