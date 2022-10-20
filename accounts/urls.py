from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.signin, name="login"),
    path("edit/", views.edit, name="edit"),
    path("mypage/", views.mypage, name="mypage"),
    path("logout/", views.signout, name="logout"),
    path("<str:username>/", views.profile, name="profile"),
    path("<int:user_pk>/follow/", views.follow, name="follow"),
]
