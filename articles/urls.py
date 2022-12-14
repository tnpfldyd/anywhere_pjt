from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path('<int:article_pk>/comment', views.comment, name='comment'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]