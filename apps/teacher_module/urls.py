from django.urls import path
from . import views
app_name= "teacher"
urlpatterns = [
    path("teachers-list/<slug:slug>", views.teacher_view.as_view(), name="teachers")
]
