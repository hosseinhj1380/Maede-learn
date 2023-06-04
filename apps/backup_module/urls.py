from django.urls import  path
from . import  views
app_name = "backup"
urlpatterns = [
    path('info',views.InfoView.as_view(),name="info-page")
]