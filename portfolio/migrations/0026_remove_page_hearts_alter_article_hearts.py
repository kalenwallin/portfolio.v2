# Generated by Django 4.1.3 on 2023-03-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0025_article_hearts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='hearts',
        ),
        migrations.AlterField(
            model_name='article',
            name='hearts',
            field=models.ManyToManyField(blank=True, related_name='page_hearts', to='portfolio.lover'),
        ),
    ]
