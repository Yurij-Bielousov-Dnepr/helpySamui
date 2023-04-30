from django.contrib import admin
from art_event.models import Article, Event

# admin.site.register(Article)
# admin.site.register(Event)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass