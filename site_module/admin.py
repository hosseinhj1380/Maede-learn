from django.contrib import admin
from .models import SiteSetting

# Register your models here.

@admin.register(SiteSetting)
class WebsiteAdmin(admin.ModelAdmin):
    pass