from django.apps import AppConfig


class WebsiteModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.site_module'

    verbose_name = "تنظیمات سایت "