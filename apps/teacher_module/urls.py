
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import teacher_view

urlpatterns = [
    path("teachers-list",teacher_view,name="teachers-list")
]
