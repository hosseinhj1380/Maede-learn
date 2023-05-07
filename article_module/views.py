from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from .models import ArticleCategory, Article


# Create your views here.


class ArticlesView(ListView):
    template_name = 'article_module/articles_page.html'
    paginate_by = 3
    context_object_name = "article"
    model = Article

    def get_queryset(self):
        data = super(ArticlesView, self).get_queryset()
        articles_data = data.filter(is_active=True)
        return articles_data


class ArticleDetailView(DetailView):
    template_name = "article_module/article-detail.html"
    context_object_name = 'article'
    model = Article

