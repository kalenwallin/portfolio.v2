# Generated by Django 4.1.3 on 2023-08-24 12:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0036_alter_post_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="cover",
            field=models.URLField(blank=True, default="", null=True),
        ),
    ]
