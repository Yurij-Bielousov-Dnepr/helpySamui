from django.contrib import admin
from accounts.models import Sponsor, Stats, MyUser, Language, SupportLevel, Region, Level, Favorites
from helpy.models import HelpRequestLanguage

# admin.site.register(Sponsor)
# admin.site.register(Stats)
# admin.site.register(MyUser)
# admin.site.register(Language)
# admin.site.register(SupportLevel)
# admin.site.register(Region)
# admin.site.register(Level)
# admin.site.register(Favorites)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    pass

@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    pass

@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(SupportLevel)
class SupportLevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    pass

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    pass

@admin.register(Language, SupportLevel, Region, HelpRequestLanguage, Level)
class HiddenAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False