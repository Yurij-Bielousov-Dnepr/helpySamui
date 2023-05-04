# models.py
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from offer.models import Helper
from art_event.models import Article, Event
from helpySamui.constants import REGION_CHOICES, LANGUAGE_CHOICES, LEVEL_CHOICES, TAG_ARTICLE_CHOICES, \
    REVIEW_RATING_CHOICES
from django.contrib.contenttypes.models import ContentType


# Re_view - для отзыва на помошника
class Re_view(models.Model):

    reviewer_name = models.CharField(max_length=255)
    helper_name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(choices=REVIEW_RATING_CHOICES)
    tag = models.CharField(choices=TAG_ARTICLE_CHOICES, max_length=100, blank=False)
    level_of_service = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)
    review_text = models.TextField()
    wishes = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Review for {self.helper_name} by {self.reviewer_name}"



    # Review - для отзыва на статью или событие
# class Review(models.Model):
#     helper = models.ForeignKey(Helper, on_delete=models.CASCADE)
#     customer_name = models.CharField(max_length=255)
#     rating = models.IntegerField(choices=REVIEW_RATING_CHOICES)
#     comment = models.TextField()
#
class Review(models.Model):
    REVIEW_TYPES = [
        ('article', 'Article'),
        ('event', 'Event'),
    ]
    review_type = models.CharField(max_length=10, choices=REVIEW_TYPES)
    content_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'content_id')
    reviewer_name = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.IntegerField(choices=REVIEW_RATING_CHOICES)
    relevance = models.IntegerField(choices=REVIEW_RATING_CHOICES, verbose_name="Relevance")
    engagement = models.IntegerField(choices=REVIEW_RATING_CHOICES, verbose_name="Engagement")

    def save(self, *args, **kwargs):
        if not self.id:
            if self.review_type == 'article':
                self.content_type = ContentType.objects.get_for_model(Article)
            elif self.review_type == 'event':
                self.content_type = ContentType.objects.get_for_model(Event)
        super().save(*args, **kwargs)

