from django.contrib import admin
from .models import SiteSetting,FooterLink,FooterLinkBox,Sliders

# Register your models here.

@admin.register(SiteSetting)
class WebsiteAdmin(admin.ModelAdmin):
    pass


admin.site.register(FooterLinkBox)
admin.site.register(FooterLink)
admin.site.register(Sliders)
