from django.db import models

from apps.user_module.models import User


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=300, verbose_name="نام دوره")
    teacher = models.ForeignKey(User, on_delete=models.CASCADE,related_name='teacher', editable=False, verbose_name="مدرس دوره")
    price = models.IntegerField(verbose_name="قیمت دوره ")
    short_description = models.CharField(max_length=150, verbose_name="توضیحات کوتاه", db_index=True)
    description = models.TextField(verbose_name="توضیحات دوره")
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
    image = models.ImageField(null=True, verbose_name="عکس دوره", upload_to="course_images")
    date_added = models.DateField(auto_created=True)
    course_length = models.IntegerField(verbose_name="زمان دوره")
    lessons = models.IntegerField(verbose_name="تعداد دروس")
    selected_categories = models.ManyToManyField("CourseCategory", verbose_name="دسته بندی ها ")

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"

    def __str__(self):
        return self.name


class CourseVisit(models.Model):
    ip = models.CharField(max_length=25, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name="کاربر")
    course = models.ForeignKey('Course', related_name='course_visit', on_delete=models.CASCADE,
                               verbose_name='دوره ')


class CourseCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')


class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name="عنوان")
    # author = models.ForeignKey
    short_description = models.CharField(max_length=150, verbose_name="توضیحات کوتاه", db_index=True)
    text = models.TextField()
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    date_added = models.DateField(auto_created=True,verbose_name="زمان انتشار")

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"

    def __str__(self):
        return self.title
