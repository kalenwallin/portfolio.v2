# Generated by Django 4.1.3 on 2023-03-17 03:08

from django.db import migrations
import markdownfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_category_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='conent',
            field=markdownfield.models.MarkdownField(blank=True, null=True, rendered_field='content_rendered'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_rendered',
            field=markdownfield.models.RenderedMarkdownField(null=True),
        ),
    ]