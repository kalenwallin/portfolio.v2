# Generated by Django 4.1.3 on 2023-08-24 12:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0037_alter_post_cover"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="cover",
        ),
    ]
