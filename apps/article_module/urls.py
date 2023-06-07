from django.urls import path

from . import views
app_name = "article"
urlpatterns = [
    path("articles", views.ArticlesView.as_view(), name="article-list"),
    path("articles/<slug:slug>", views.ArticleDetailView.as_view(), name="article-detail")
]
