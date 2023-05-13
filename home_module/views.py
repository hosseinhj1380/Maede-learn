from django.shortcuts import render
from django.views.generic import TemplateView, View
from site_module.models import Sliders


# Create your views here.

class Home_page(TemplateView):
    template_name = 'home_module/home_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super(Home_page, self).get_context_data(*args,**kwargs)
        slider: Sliders = Sliders.objects.filter(is_active=True)
        context['slider'] = slider
        return context


def header_component(request):
    return render(request, 'shared/site_header_component.html', {})


def footer_component(request):
    return render(request, 'shared/site_footer-component.html', {})
