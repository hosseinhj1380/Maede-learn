from django.db import models
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=300,verbose_name="نام دوره")
    # author = models.ForeignKey
    price = models.IntegerField(verbose_name="قیمت دوره ")
    short_description = models.CharField(max_length=150,verbose_name="توضیحات کوتاه",db_index=True)
    description = models.TextField(verbose_name="توضیحات دوره")
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')
    image = models.ImageField(null=True, verbose_name="عکس دوره", upload_to="course_images")
    date_added = models.DateField(auto_created=True)

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"

    def __str__(self):
        return self.name


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
