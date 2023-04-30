from django.contrib import admin
from offer.models import Helper

admin.site.register(Helper)

@admin.register(Helper)
class HelperAdmin(admin.ModelAdmin):
    pass