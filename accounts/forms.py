from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        labels = {
            "username": "아이디",
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "first_name",
            "last_name",
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "nickname", "image"]
