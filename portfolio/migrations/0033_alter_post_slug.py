# Generated by Django 4.1.3 on 2023-08-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0032_alter_post_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=200),
        ),
    ]
