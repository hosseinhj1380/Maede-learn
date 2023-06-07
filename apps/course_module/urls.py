from django.urls import path
from .views import CourseListView
app_name = "course"
urlpatterns = [
    path('courses', CourseListView.as_view() ,name='courses_list'),]
    # path('<slug:slug>', CourseDetailView.as_view() ,name='courses_detail')