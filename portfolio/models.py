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


class Lover(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


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
    hearts = models.ManyToManyField(Lover, related_name="page_hearts",
                                    blank=True)

    def total_hearts(self):
        return self.hearts.count()

    def __str__(self):
        return str(self.item) + "'s Page"


class Category(models.Model):
    # name of the category
    name = models.CharField(max_length=200, blank=True, null=True)
    # cdn url of the icon of the category
    icon = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    # cdn url of image cover
    image_url = models.CharField(max_length=200, blank=True, null=True)
    # name of article
    name = models.CharField(max_length=200, blank=True, null=True)
    # short description of article
    short_description = models.CharField(max_length=200, blank=True, null=True)
    # when you started work
    start_date = models.CharField(max_length=200, blank=True, null=True)
    # when you finished work
    end_date = models.CharField(max_length=200, blank=True, null=True)
    # which category this article belongs to
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 default=None, blank=True, null=True)
    # the content of this article
    conent = MarkdownField(rendered_field='content_rendered',
                           validator=VALIDATOR_STANDARD, blank=True, null=True)
    content_rendered = RenderedMarkdownField(blank=True, null=True)

    def __str__(self):
        if self.position:
            return str(self.name) + " - " + str(self.position)
        elif self.short_description:
            return str(self.name) + " - " + str(self.short_description)
        else:
            return str(self.name)
