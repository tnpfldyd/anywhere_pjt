from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm, ProfileForm, CustomUserChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

# Create your views here.


def index(request):
    return render(request, "accounts/index.html")


def profile(request, username):
    info = get_object_or_404(get_user_model(), username=username)
    return render(request, "accounts/profile.html", {"person": info})


def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect("accounts:index")
    return render(request, "accounts/signup.html", {"form": form})


def signin(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect("accounts:index")
    return render(request, "accounts/login.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("articles:index")


def profile_edit(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
