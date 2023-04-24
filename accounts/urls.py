from django.urls import path, include
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
from .views import VIPView

app_name = "accounts"  # добавьте это, если используете пространства имен


urlpatterns = [
    path("account_inactive/", views.account_inactive, name="account_inactive"),
    path("email/", views.email, name="email"),
    path("email_confirm/", views.email_confirm, name="email_confirm"),
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path("password_change/", views.password_change, name="password_change"),
    path("password_reset/", views.password_reset, name="password_reset"),
    path("password_reset_done/", views.password_reset_done, name="password_reset_done"),
    path("password_reset_from_key/", views.password_reset_from_key, name="password_reset_from_key"),
    path("password_reset_from_key_done/", views.password_reset_from_key_done, name="password_reset_from_key_done"),
    path("password_set/", views.password_set, name="password_set"),
    path("sign_in/", views.sign_in, name="account_sign_in"),
    path("signup/", views.signup, name="account_signup"),
    path("signup_closed/", views.signup_closed, name="signup_closed"),
    path("verification_sent/", views.verification_sent, name="verification_sent"),
    path("verified_email_required/", views.verified_email_required, name="verified_email_required"),
    path( 'vip/', VIPView.as_view(), name='vip' ),

]
    #    path( 'set_webhook/', set_webhook ),
    #    path('webhook/', webhook, name='webhook'),
    #    path('telegram_bot/', telegram_bot, name='telegram_bot'),

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
