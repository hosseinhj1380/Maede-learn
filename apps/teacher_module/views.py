from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from django.http import HttpResponse

def teacher_view(request):
    return HttpResponse("hello world ")

