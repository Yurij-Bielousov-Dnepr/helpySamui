from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.contrib import admin

# from telegram_bot.views import webhook, telegram_bot
# from telegram_bot.telegram_bot import set_webhook, webhook
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from .views import (
    review_helper,
    ReviewCreateView,
    ModerateReview,
    review_edit,
    review_list_helper,
    review_detail,
)

app_name = "reviews"  # добавьте это, если используете пространства имен
'reviews_add'
'reviews_list'

urlpatterns = [
    path("reviews/review_helper/", review_helper, name="review_helper"),
    path( 'review_edit/<int:pk>/', review_edit, name='review_edit' ),
    path( "reviews/add/", ReviewCreateView.as_view(), name="reviews_add" ),
    path( "reviews/", review_list_helper, name="reviews_list" ),
    path("reviews/<int:pk>/", review_detail, name="review_detail"),
    path(
        "reviews/moderate/",
        staff_member_required(ModerateReview.as_view()),
        name=" moderation_view",
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
