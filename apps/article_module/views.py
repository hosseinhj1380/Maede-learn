from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView,FormView,CreateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from .models import ArticleCategory, Article
from ..user_module.models import User


# from .forms import CommentForm

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
    model = Article
    context_object_name = 'article'
    fields = '__all__'
    success_url = '/'

    def get_context_data(self,*args,**kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['user'] = User.objects.filter(is_active=True).first()
        return context



