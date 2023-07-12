from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView, View

from apps.course_module.models import Course
from apps.site_module.models import Sliders



# Create your views here.

class Home_page(TemplateView):
    template_name = 'home_module/home_page.html'

    def get_context_data(self,*args, **kwargs):
        context = super(Home_page, self).get_context_data(**kwargs)
        slider: Sliders = Sliders.objects.active_sliders()
        context['slider'] = slider
        context['most_viewed'] = Course.objects.annotate(number_of_visits=Count('course_visit')).filter(is_active=True,is_delete=False).order_by('-number_of_visits')[:4]
        latest_products = Course.objects.filter(is_active=True, is_delete=False).order_by('-id')[:4]
        context['latest_products'] = latest_products
        return context


def header_component(request):
    return render(request, 'shared/site_header_component.html', {})


def footer_component(request):
    return render(request, 'shared/site_footer-component.html', {})
