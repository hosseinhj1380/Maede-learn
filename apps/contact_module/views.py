import django.views.generic
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import FormView, CreateView
from .forms import ContactUsModelForm


# Create your views here.


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us.html'
    form_class = ContactUsModelForm
    success_url = '/'



