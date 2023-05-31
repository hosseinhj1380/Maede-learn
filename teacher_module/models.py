from django.db import models

# Create your models here.
class teachers(models.Model):
    Full_name=models.CharField(max_length=50,null=False,blank=False,verbose_name="  نام و نام خانوادگی مدرس")
    Expertise=models.CharField(max_length=25,null=False,blank=False,verbose_name="مهارت")
    NumberofCorses=models.IntegerField(null=False,blank=False,verbose_name="تعداد دوره ها ")
    is_active=models.BooleanField(default=False,verbose_name="فعال/غیرفعال")
    About_teacher=models.TextField(null=False,blank=False,verbose_name="درباره مدرس")
    Image=models.ImageField(null=True, verbose_name="عکس مدرس", upload_to="teacher_images")


    class Meta:
        verbose_name = "مدرسین"
        verbose_name_plural = "مدرسین"
    def __str__(self):
        return self.Full_name