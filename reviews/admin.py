from django.contrib import admin
from reviews.models import Review, Re_view

# admin.site.register(Review)
# admin.site.register(Re_view)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Re_view)
class Re_viewAdmin(admin.ModelAdmin):
    pass