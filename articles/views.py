from django.shortcuts import render, redirect
from .models import Article, Comment
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    recents = Article.objects.order_by("-pk")
    likes = Article.objects.order_by("-article_liking")

    context = {
        "recents": recents,
        "likes": likes,
    }

    return render(request, "articles/index.html", context)


@login_required
def create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.user_id = request.user.id
        temp.save()
        return redirect("articles:detail", temp.id)
    return render(request, "articles/create.html", {"form": form})


def detail(request, pk):
    context = {"article": get_object_or_404(Article, pk=pk), "comment": CommentForm()}
    return render(request, "articles/detail.html", context)


@login_required
def comment(request, article_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.article_id = article_pk
        temp.user_id = request.user.id
        temp.save()
        return redirect("articles:detail", article_pk)


def comment_delete(request, article_pk, comment_pk):
    temp = (get_object_or_404(Comment, pk=comment_pk),)
    if request.user.id == temp.user_id:
        temp.delete()
        return redirect("articles:detail", article_pk)
    else:
        return HttpResponseForbidden
