from django import forms
from django.utils.translation import gettext as _
import reviews
from .models import Helper, ReviewHelper, ReviewArt_Event
from art_event.models import Article, Event, Review, Tag_article
from accounts.models import *
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.contenttypes.models import ContentType
from helpySamui.constants import REGION_CHOICES, LANGUAGE_CHOICES, LEVEL_CHOICES, TAG_ARTICLE_CHOICES, \
    REVIEW_RATING_CHOICES, TAG_HELP_NAME_CHOICES


class ReviewHelperCreateForm(forms.ModelForm):
    class Meta:
        model = ReviewHelper
        fields = ["reviewer_name", "helper_name", "rating", "tag", "level_of_service", "review_text", "wishes"]
        labels = {
            "reviewer_name": _("Reviewer Name"),
            "helper_name": _("Helper Name"),
            "rating": _("Rating"),
            "tag": _("Tag"),
            "level_of_service": _("Level of Service"),
            "review_text": _("Review Text"),
            "wishes": _("Wishes"),
        }
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "tag": forms.Select(choices=TAG_HELP_NAME_CHOICES),
            "level_of_service": forms.Select(choices=LEVEL_CHOICES),
        }

class ReviewHelperEditForm(forms.ModelForm):
    class Meta:
        model = ReviewHelper
        fields = ["reviewer_name", "helper_name", "rating", "tag", "level_of_service", "review_text", "wishes"]
        labels = {
            "reviewer_name": _("Your Name"),
            "helper_name": _("Helper's Name"),
            "rating": _("Rating"),
            "tag": _("Tag"),
            "level_of_service": _("Level of Service"),
            "review_text": _("Review Text"),
            "wishes": _("Wishes"),
        }
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "level_of_service": forms.RadioSelect(choices=LEVEL_CHOICES),
            "tag": forms.RadioSelect(choices=TAG_HELP_NAME_CHOICES),
        }
class ReviewForm_Art_Event(forms.ModelForm):
    REVIEW_TYPES = [
        ('article', 'Article'),
        ('event', 'Event'),
    ]
    review_type = forms.ChoiceField(choices=REVIEW_TYPES)
    content_id = forms.IntegerField()
    reviewer_name = forms.CharField(max_length=255)
    comment = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 5}))
    relevance = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 5}))
    engagement = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 5}))

    class Meta:
        model = Review
        fields = ['review_type', 'content_id', 'reviewer_name', 'comment', 'rating', 'relevance', 'engagement']

    def clean(self):
        cleaned_data = super().clean()
        review_type = cleaned_data.get('review_type')
        content_id = cleaned_data.get('content_id')

        if review_type == 'article':
            try:
                Article.objects.get(pk=content_id)
            except Article.DoesNotExist:
                raise forms.ValidationError('Article does not exist')
        elif review_type == 'event':
            try:
                Event.objects.get(pk=content_id)
            except Event.DoesNotExist:
                raise forms.ValidationError('Event does not exist')
        else:
            raise forms.ValidationError('Invalid review type')

        return cleaned_data
class ReviewFormEdit_Art_Event(forms.ModelForm):
    REVIEW_TYPES = [
        ('article', 'Article'),
        ('event', 'Event'),
    ]
    review_type = forms.ChoiceField(choices=REVIEW_TYPES)
    content_id = forms.IntegerField()
    reviewer_name = forms.CharField(max_length=255)
    comment = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 5}))
    relevance = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 5}))
    engagement = forms.IntegerField(widget=forms.NumberInput(attrs={'min': 1, 'max': 5}))

    class Meta:
        model = ReviewArt_Event
        fields = ['review_type', 'content_id', 'reviewer_name', 'comment', 'rating', 'relevance', 'engagement']

    def clean(self):
        cleaned_data = super().clean()
        review_type = cleaned_data.get('review_type')
        content_id = cleaned_data.get('content_id')

        if review_type == 'article':
            try:
                Article.objects.get(pk=content_id)
            except Article.DoesNotExist:
                raise forms.ValidationError('Article does not exist')
        elif review_type == 'event':
            try:
                Event.objects.get(pk=content_id)
            except Event.DoesNotExist:
                raise forms.ValidationError('Event does not exist')
        else:
            raise forms.ValidationError('Invalid review type')

        return cleaned_data


class ArticleModerationForm(forms.ModelForm):
    action = forms.ChoiceField(choices=(('approve', 'Approve'), ('edit', 'Edit'), ('delete', 'Delete')))

    class Meta:
        model = Article
        fields = ['title', 'text']


class EventModerationForm(forms.ModelForm):
    CHOICES = [
        ('approve', 'Approve'),
        ('edit', 'Edit'),
        ('delete', 'Delete'),
    ]
    action = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Event
        fields = []


class ReviewHelperModerationForm(forms.ModelForm):
    CHOICES = [
        ('approve', 'Approve'),
        ('edit', 'Edit'),
        ('delete', 'Delete'),
    ]
    action = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = ReviewHelper
        fields = []
