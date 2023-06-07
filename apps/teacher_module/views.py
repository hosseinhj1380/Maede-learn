from django.shortcuts import render
from django.views.generic import View,ListView,TemplateView,DetailView
# Create your views here.
from django.http import HttpResponse
from .models import teachers


class teacher_view(ListView):
    template_name="teacher_module/teacher-single.html"
    model=teachers
    context_object_name="teachers"


