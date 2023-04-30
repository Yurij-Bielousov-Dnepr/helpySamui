from django.contrib import admin
from art_event.models import Article, Event
from .models import Tag_article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "Tag_article":
            kwargs["queryset"] = Tag_article.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "Tag_article":
            kwargs["queryset"] = Tag_article.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)