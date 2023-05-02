# models.py
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
from accounts.models import MyUser


class Tag_article(models.Model):
    MOTO_RENT = 'moto_rent'
    MOTO_BEGINNER = 'moto_beginner'
    MOTO_SOS = 'moto_sos'
    RENT_ESTATE = 'rent_estate'
    PUBLIC_SERV = 'public_serv'
    LANG_SCHOL = 'lang_schol'
    MED_HELP = 'med_help'
    SERV_TRANSL = 'serv_transl'
    SHOPPING_DESTINATION = 'shopping_destination'
    SOUVENIRS = 'souvenirs'

    NAME_CHOICES = (
        (MOTO_RENT, _("Moto Rent")),
        (MOTO_BEGINNER, _("Moto Beginner")),
        (MOTO_SOS, _("Moto SOS")),
        (RENT_ESTATE, _("Rent Estate")),
        (PUBLIC_SERV, _("Public Service")),
        (LANG_SCHOL, _("Language School")),
        (MED_HELP, _("Medical Help")),
        (SERV_TRANSL, _("Translation Services")),
        (SHOPPING_DESTINATION, _("Shopping Destination")),
        (SOUVENIRS, _("Souvenirs")),
    )

    name = models.CharField(max_length=20, choices=NAME_CHOICES)

    def __str__(self):
        return self.get_name_display()

    class Meta:
        app_label = 'art_event'

class Event(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=75)
    rating = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag_article, default='moto_rent', verbose_name="Tags")

    def clean(self):
        super().clean()
        if not self.tags.exists():
            raise ValidationError('At least one tag is required.')



class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    rating = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag_article, default='moto_rent', verbose_name="Tags")

    def clean(self):
        super().clean()
        if not self.tags.exists():
            raise ValidationError('At least one tag is required.')

class Review(models.Model):
    RATING_CHOICES = (
        (1, "1 star"),
        (2, "2 stars"),
        (3, "3 stars"),
        (4, "4 stars"),
        (5, "5 stars"),
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=255)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField()
    relevance = models.IntegerField( choices=RATING_CHOICES, verbose_name="Relevance" )
    engagement = models.IntegerField( choices=RATING_CHOICES, verbose_name="Engagement" )

class Favorites(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, null=True, blank=True
    )
    is_favorite = models.BooleanField(default=False)


