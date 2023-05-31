from django.contrib import admin
from .models import teachers
# Register your models here.
@admin.register(teachers)
class teachers(admin.ModelAdmin):
    list_display=["Full_name","Expertise","NumberofCorses","is_active","About_teacher","Image"]
    list_editable=["is_active"]