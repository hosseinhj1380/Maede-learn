from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
# from django.http import HttpResponse
from .models import teachers


class teacher_view(DetailView):
    template_name="teacher_module/teacher-single.html"
    model=teachers
    context_object_name="teacher"
    

class teacher_lists(ListView):
    template_name="teacher_module/teachers_list.html"
    model=teachers
    context_object_name="teachers"
