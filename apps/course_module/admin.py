from django.contrib import admin
from django.http import HttpRequest

from .models import Course, Blog, CourseCategory


# Register your models here.

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # list_filter = ['', 'is_active']
    prepopulated_fields = {'slug': ["name", ]}
    list_display = ('name', 'price', 'is_active', 'teacher')
    list_editable = ('price', 'is_active')

    def save_model(self, request: HttpRequest, obj, form, change):
        if not change:
            obj.teacher = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # list_filter = ['', 'is_active']
    prepopulated_fields = {'slug': ["title", ]}
    list_display = ('__str__', 'short_description', 'date_added', 'is_active')
    list_editable = ('short_description', 'is_active',)
