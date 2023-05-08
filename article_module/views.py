from django.shortcuts import render
from django.views.generic import DetailView,FormView,CreateView
from django.views.generic.edit import FormMixin
from django.views.generic.list import ListView
from .models import ArticleCategory, Article,Comments
from .forms import CommentForm

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


class ArticleDetailView(DetailView,CreateView):
    template_name = "article_module/article-detail.html"
    model = Article
    context_object_name = 'article'
    form_class=CommentForm
    success_url = '/'


# def comment_component(request):
#     context = {
#         "comment" : Comments.objects.all()
#     }
#     render(request,'article_module/comments.html', context)