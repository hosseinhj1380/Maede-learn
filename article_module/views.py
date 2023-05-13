from django.shortcuts import render
from django.views.generic import DetailView,FormView,CreateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from .models import ArticleCategory, Article,Comments
from .forms import CommentForm

# Create your views here.


class ArticlesView(ListView):
    template_name = 'article_module/articles_page.html'
    paginate_by = 4
    context_object_name = "article"
    formclass = CommentForm
    model = Article

    def get_queryset(self):
        data = super(ArticlesView, self).get_queryset()
        articles_data = data.filter(is_active=True)
        return articles_data


class ArticleDetailView(DetailView):
    template_name = "article_module/article-detail.html"
    model = Article
    context_object_name = 'article'


def get_context_data(self, **kwargs):
    context = super(ArticleDetailView, self).get_context_data(**kwargs)
    article = kwargs.get('object')
    comment: Comments = Comments.objects.filter(article_id=article.id, parent=None).prefetch_related(
        "article__articlecomments_set")

    context['comments'] = comment
    return context


