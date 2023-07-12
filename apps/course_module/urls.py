from django.urls import path
from . import views
app_name = "course"
urlpatterns = [
    path('courses_list/', views.CourseListView.as_view() ,name='courses_list'),
    path('courses_list/cat/<str:category>', views.CourseListView.as_view() ,name='courses_list_by_cat'),
    path('courses_list/<slug:slug>', views.CourseDetailView.as_view() ,name='courses_detail'),



]
