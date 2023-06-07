from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course


# Create your views here.


class CourseListView(ListView):
    template_name = 'course_module/courselist.html'
    context_object_name = "courses"
    model = Course
    paginate_by = 2
    ordering = ['price']

    def get_queryset(self):
        base_query = super(CourseListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data


class CourseDetailView(DetailView):
    template_name = 'course_module/course-detail.html'
    model = Course
    context_object_name = 'course'
