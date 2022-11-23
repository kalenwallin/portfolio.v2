from django.db import models

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
    row = models.ForeignKey(Row, on_delete=models.CASCADE, default=None, blank=True, null=True)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Lover(models.Model):
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip

class Page(models.Model):
    story = models.TextField(blank=True)
    pdf = models.FileField(upload_to='page/pdf', default='empty', blank=True)
    iframe = models.TextField(blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    is_game = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    author = models.TextField(blank=True)
    hearts = models.ManyToManyField(Lover, related_name="page_hearts", blank=True)

    def total_hearts(self):
        return self.hearts.count()

    def __str__(self):
        return str(self.item) + "'s Page"
