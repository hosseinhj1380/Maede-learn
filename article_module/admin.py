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

    def save_model(self, request, obj, form, change):
        if not change :
            obj.author = request.user
        return super().save_model(request,obj,form,change)

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
   pass
