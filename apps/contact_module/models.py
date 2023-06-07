from django.db import models


# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=300, verbose_name="نام و نام خانوادگی")
    title = models.CharField(max_length=300, verbose_name="عنوان")
    site = models.CharField(max_length=300, verbose_name="وبسایت")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="متن تماس با ما")
    response = models.CharField(max_length=300, verbose_name="پاسخ تماس با ما")
    created_at = models.DateTimeField(verbose_name="زمان انتشار", auto_now_add=True)
    is_read_by_admin = models.BooleanField(default=False, verbose_name="خوانده شده توسط ادمین")

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "لیست تماس ها با ما"

    def __str__(self):
        return self.title
