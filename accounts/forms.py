from django import forms
from django.contrib.auth.views import PasswordChangeView
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.views.generic import CreateView
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation


class EmailForm(forms.Form):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )

    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label='Confirm new password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    class Meta:
        fields = ['old_password', 'new_password1', 'new_password2']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = ("userNick", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = 'accounts:verification_sent'  # замените на ваш URL

class PasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'accounts/password_change.html'
    success_url = 'accounts:password_change_done'  # замените на ваш URL
class EditVisitorProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            "userNick",
            "category",
            "district",
            "languages",
            "phone_number",
            "email",
            "about_me",
        )


class AddEmailForm(forms.Form):
    email = forms.EmailField(label=_("Email address"))


class RemoveEmailForm(forms.Form):
    email = forms.EmailField(label=_("Email address to remove"))


class CustomAuthenticationForm(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ["email", "password"]


class VisitorForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            "userNick",
            "category",
            "district",
            "languages",
            "is_sponsor",
            "phone_number",
            "email",
            ]
        widgets = {
            "district": forms.CheckboxSelectMultiple(),
            "languages": forms.CheckboxSelectMultiple(),
            # "favorites": forms.SelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", "Save"))
