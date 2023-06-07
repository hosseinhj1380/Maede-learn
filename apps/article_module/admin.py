from django.contrib import admin
from .models import ArticleCategory, Article,Comments


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'parent', 'is_active']
    list_editable = ['is_active', 'url', 'parent']


@admin.register(Article)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active' ]
    prepopulated_fields = {"slug": ['title',]}

@admin.register(Comments)
class Commentsadmin(admin.ModelAdmin):
    list_display = ['full_name','message','email']
