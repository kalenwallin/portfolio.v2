# Generated by Django 4.1.3 on 2023-08-24 13:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0039_post_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=200, null=True),
        ),
    ]
