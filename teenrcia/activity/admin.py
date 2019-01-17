from django.contrib import admin

from .models import Activity, Section, Item, Post, Comment, ImageQuote


class SectionInline(admin.StackedInline):
    model = Section
    extra = 3


class ItemInline(admin.StackedInline):
    model = Item
    extra = 3


class ActivityAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


admin.site.register(Activity, ActivityAdmin)
admin.site.register(Item)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(ImageQuote)

