from django.contrib import admin

from .models import Item, Page, Row, Lover, Category, Article

admin.site.register(Item)
admin.site.register(Row)
admin.site.register(Lover)
admin.site.register(Category)
admin.site.register(Article)


class PageAdmin(admin.ModelAdmin):
    model = Page
    fields = ['story', 'pdf', 'iframe', 'item', 'is_game', 'slug', 'author',
              'hearts']


admin.site.register(Page, PageAdmin)
