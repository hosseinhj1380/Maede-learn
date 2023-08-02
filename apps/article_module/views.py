from django.db.models import Count
from django.http import HttpRequest
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
    paginate_by = 1
    context_object_name = "article"
    model = Article
    ordering = "date"

    def get_queryset(self):
        data = super(ArticlesView, self).get_queryset()
        this_category = self.kwargs.get('category')
        if this_category is not None :
            data = data.filter(selected_categories__title__iexact=this_category)
        data = data.filter(is_active=True).order_by('date')
        return data


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


def article_categories_component(request:HttpRequest):
    categories = ArticleCategory.objects.filter(is_active=True, parent=None).annotate(
        aricle_count=Count("article"))
    context = {
        'categories' : categories

    }
    return render(request,"article_module/components/article_category_component.html",context)

def latest_articles_components(request:HttpRequest):
    articles : Article = Article.objects.filter(is_active=True).order_by('-date')[:5]
    context = {
        'latest_articles' : articles
    }
    return render(request, "article_module/components/latest_articles_components.html", context)