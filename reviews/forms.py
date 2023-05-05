from django import forms
from django.utils.translation import gettext as _
import reviews
from .models import Helper, Review, Re_view
from art_event.models import Article, Event, Review, Tag_article
from accounts.models import *
from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.contenttypes.models import ContentType
from helpySamui.constants import REGION_CHOICES, LANGUAGE_CHOICES, LEVEL_CHOICES, TAG_ARTICLE_CHOICES, \
    REVIEW_RATING_CHOICES



# class ReviewForm(forms.ModelForm):
#     rating = forms.ChoiceField(
#         choices=Re_view.RATING_CHOICES,
#         widget=forms.RadioSelect(attrs={"class": "form-check-input"}),
#     )
#     level_of_service = forms.ChoiceField(
#         choices=Re_view.LEVEL_CHOICES,
#         widget=forms.RadioSelect(attrs={"class": "form-control"}),
#     )
#     review_text = forms.CharField(
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )
#     wishes = forms.CharField(
#         required=False, widget=forms.TextInput(attrs={"class": "form-control"})
#     )
#     tag = forms.ChoiceField(
#         choices=Re_view.TAG_CHOICES,
#         widget=forms.Select(attrs={"class": "form-control"}),
#     )
#
#     class Meta:
#         model = Re_view
#         fields = [
#             "reviewer_name",
#             "helper_name",
#             "tag",
#             "rating",
#             "level_of_service",
#             "review_text",
#             "wishes",
#         ]
#         widgets = {
#             "reviewer_name": forms.TextInput(attrs={"class": "form-control"}),
#             "helper_name": forms.TextInput(attrs={"class": "form-control"}),
#             "rating": forms.RadioSelect(attrs={"class": "form-control"}),
#             "tag": forms.Select(attrs={"class": "form-control"}),
#             "level_of_service": forms.RadioSelect(attrs={"class": "form-control"}),
#             "review_text": forms.TextInput(attrs={"class": "form-control"}),
#             "wishes": forms.TextInput(attrs={"class": "form-control"}),
#         }
#
#     def clean(self):
#         cleaned_data = super().clean()
#         reviewer_name = cleaned_data.get("reviewer_name")
#         helper_name = cleaned_data.get("helper_name")
#         rating = cleaned_data.get("rating")
#         tag = cleaned_data.get("tag")
#         level_of_service = cleaned_data.get("level_of_service")
#         review_text = cleaned_data.get("review_text")
#         wishes = cleaned_data.get("wishes")
#         if (
#             not reviewer_name
#             or not helper_name
#             or not rating
#             or not tag
#             or not level_of_service
#             or not review_text
#         ):
#             raise forms.ValidationError(
#                 "All fields are required", code="required_fields"
#             )

class Review_editForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'comment', 'rating']
        widgets = {

            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'}),
        }
class ReviewForm(forms.ModelForm):
    class Meta:
        model = reviews.models.Review
        fields = ["customer_name", "rating", "comment"]
        labels = {
            "customer_name": _("Helper Nickname"),
            "rating": _("Rate"),
            "comment": _("Comment"),
        }
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
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
