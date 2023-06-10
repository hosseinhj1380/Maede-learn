from django.contrib import admin
from .models import teachers,TalentCategory
# Register your models here.
@admin.register(teachers)
class teachers(admin.ModelAdmin):
    list_display=["Full_name","talent","NumberofCorses","is_active","About_teacher","Image"]
    list_editable=["is_active"]

@admin.register(TalentCategory)
class talentcategory(admin.ModelAdmin):
    list_display=["title","url","is_active"]
    list_editable=["is_active"]