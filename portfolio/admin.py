from django.contrib import admin

from .models import Item, Page, Row, Lover

admin.site.register(Item)
admin.site.register(Row)
admin.site.register(Lover)

class PageAdmin(admin.ModelAdmin):
    model = Page
    fields = ['story', 'pdf', 'iframe', 'item', 'is_game', 'slug', 'author', 'hearts']

admin.site.register(Page, PageAdmin)