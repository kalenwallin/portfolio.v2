# Generated by Django 4.1.3 on 2023-02-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_remove_page_created_on_remove_page_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created_on',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='page',
            name='updated_on',
            field=models.TextField(blank=True),
        ),
    ]
