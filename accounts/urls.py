from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.signin, name="login"),
    path("logout/", views.signout, name="logout"),
    path("<str:username>/", views.profile, name="profile"),
    path("profile_edit/", views.profile_edit, name="profile_edit"),
]
