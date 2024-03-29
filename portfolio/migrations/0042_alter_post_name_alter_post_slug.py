# Generated by Django 4.1.3 on 2023-08-24 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("portfolio", "0041_alter_post_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="name",
            field=models.CharField(blank=True, default=None, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(max_length=400, null=True),
        ),
    ]
