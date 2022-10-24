from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/send", views.send, name="send"),
    path("<int:room_pk>/detail", views.detail, name="detail"),
]
