from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


# Create your views here.

class InfoView(TemplateView):
    template_name = 'backup_module/info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date"] = "this is gonna give template some date "
