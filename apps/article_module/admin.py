from django.contrib import admin
from .models import ArticleCategory, Article , Comments


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'parent', 'is_active']
    list_editable = ['is_active', 'url', 'parent']


@admin.register(Article)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active' ]
    prepopulated_fields = {"slug": ['title',]}
    exclude = ('writer',)  # Exclude the writer field from the admin form

    def save_model(self, request, obj, form, change):
        if not change :
            obj.writer = request.user
        return super().save_model(request,obj,form,change)


@admin.register(Comments)
class Commentsadmin(admin.ModelAdmin):
    list_display = ['full_name','message','email']




