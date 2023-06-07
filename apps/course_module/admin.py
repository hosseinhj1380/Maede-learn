from django.contrib import admin
from .models import Course, Blog


# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # list_filter = ['', 'is_active']
    prepopulated_fields = {'slug': ["name", ]}
    list_display = ('name', 'price', 'is_active', 'is_delete')
    list_editable = ('price', 'is_active')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    # list_filter = ['', 'is_active']
    prepopulated_fields = {'slug': ["title", ]}
    list_display = ( '__str__','short_description','date_added','is_active')
    list_editable = ('short_description', 'is_active',)


