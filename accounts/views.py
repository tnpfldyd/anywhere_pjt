from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .forms import CustomUserCreationForm, ProfileForm, CustomUserChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    users = get_user_model().objects.all()
    return render(request, "accounts/index.html", {"users": users})


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
    return redirect("accounts:index")


@login_required
def edit(request):
    if request.method == "POST":
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_change_form.is_valid():
            user = user_change_form.save()
            profile_form.save()
            return redirect("accounts:profile", user.username)
        return redirect("accounts:edit")
    user_change_form = CustomUserChangeForm(instance=request.user)
    pro, create = Profile.objects.get_or_create(user=request.user)
    profile_form = ProfileForm(instance=pro)
    context = {
        "user_change_form": user_change_form,
        "profile_form": profile_form,
    }
    return render(request, "accounts/edit.html", context)


def mypage(request):
    return render(request, "accounts/mypage.html")


@login_required
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect("accounts:profile", person.username)
