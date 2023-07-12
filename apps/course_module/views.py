from django.db.models import Count
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from utils.group_slicer import list_group
from utils.http_service import get_ip
from .models import Course, CourseCategory, CourseVisit


# Create your views here.


class CourseListView(ListView):
    template_name = 'course_module/courselist.html'
    context_object_name = "courses"
    model = Course
    paginate_by = 6
    ordering = ['-price']

    def get_queryset(self):
        base_query = super(CourseListView, self).get_queryset()
        this_category = self.kwargs.get('category')
        if this_category is not None:
            base_query = base_query.filter(selected_categories__url_title__iexact=this_category, is_active=True)

        return base_query

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        request: HttpRequest = self.request
        context['categories'] = CourseCategory.objects.annotate(product_categories=Count('course')).filter(
            is_delete=False, is_active=True).order_by('-product_categories')

        return context


class CourseDetailView(DetailView):
    template_name = 'course_module/course-detail.html'
    model = Course
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data()
        course: Course = kwargs.get('object')
        teacher_related_courses = list(Course.objects.filter(is_delete=False,is_active=True,teacher_id=course.teacher_id).exclude(pk=course.id).order_by('-id'))[:4]
        context['teacher_related_courses'] = list_group(teacher_related_courses,4)
        user_id = None
        user_ip = get_ip(self.request)
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = CourseVisit.objects.filter(ip__iexact=user_ip , course_id=course.id,user__exact=user_id).exists()
        if not has_been_visited:
            new_visit = CourseVisit(ip=user_ip,user_id=user_id, course_id=course.id)
            new_visit.save()
        return context
