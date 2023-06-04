from django.urls import path
from . import views

app_name= "contact"
urlpatterns = [
path('contact-us', views.ContactUsView.as_view(), name='contact-us')
]
