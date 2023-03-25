from autoslug import AutoSlugField
from django.db import models

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD


class Row(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(default="default_icon.png")
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Item(models.Model):
    cover_image = models.ImageField()
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    row = models.ForeignKey(Row, on_delete=models.CASCADE, default=None,
                            blank=True, null=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class Page(models.Model):
    story = models.TextField(blank=True, null=True)
    pdf = models.FileField(upload_to='page/pdf', default='empty', blank=True,
                           null=True)
    iframe = models.TextField(blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_game = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.TextField(blank=True)

    def __str__(self):
        return str(self.item) + "'s Page"


class Category(models.Model):
    # name of the category
    name = models.CharField(max_length=200, blank=True, null=True)
    # cdn url of the icon of the category
    icon = models.CharField(max_length=200, blank=True, null=True)
    # priority of the category
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Article(models.Model):
    # cdn url of image cover
    image_url = models.CharField(max_length=200, blank=True, null=True)
    # name of article
    name = models.CharField(max_length=200, blank=True, null=True)
    # which category this article belongs to
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 default=None, blank=True, null=True)
    # url slug generated from the name of the article
    slug = AutoSlugField(populate_from='name', blank=True, null=True)
    # url slug for v3 article
    v3slug = models.CharField(max_length=200, blank=True, null=True)
    # priority of the article
    order = models.IntegerField(default=1)

    def __str__(self):
        if self.short_description:
            return str(self.name) + " - " + str(self.short_description)
        else:
            return str(self.name)
