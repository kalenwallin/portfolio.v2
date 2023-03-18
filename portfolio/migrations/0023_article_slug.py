# Generated by Django 4.1.3 on 2023-03-18 08:30

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_category_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='name'),
        ),
    ]