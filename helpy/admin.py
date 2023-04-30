from django.contrib import admin
from helpy.models import Tag_help, HelpRequest, HelpRequestLanguage

admin.site.register(Tag_help)
admin.site.register(HelpRequest)
admin.site.register(HelpRequestLanguage)

@admin.register(Tag_help)
class Tag_helpAdmin(admin.ModelAdmin):
    pass

@admin.register(HelpRequest)
class HelpRequestAdmin(admin.ModelAdmin):
    pass

@admin.register(HelpRequestLanguage)
class HelpRequestLanguageAdmin(admin.ModelAdmin):
    pass