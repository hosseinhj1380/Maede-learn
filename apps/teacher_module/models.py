from django.db import models

# Create your models here.
class teachers(models.Model):
    Full_name=models.CharField(max_length=50,null=False,blank=False,verbose_name="  نام و نام خانوادگی مدرس")
    # Expertise=models.CharField(max_length=25,null=False,blank=False,verbose_name="مهارت")
    NumberofCorses=models.IntegerField(null=False,blank=False,verbose_name="تعداد دوره ")
    is_active=models.BooleanField(default=False,verbose_name="فعال/غیرفعال")
    About_teacher=models.TextField(null=False,blank=False,verbose_name="درباره مدرس")
    Image=models.ImageField(null=True, verbose_name="عکس مدرس", upload_to="teacher_images")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="عنوان در URL",default='')
    talent=models.ForeignKey("TalentCategory",verbose_name="مهارت استاد ",on_delete=models.CASCADE,default=True)


    class Meta:
        verbose_name = "مدرسین"
        verbose_name_plural = "مدرسین"
    def __str__(self):
        return self.Full_name


class TalentCategory(models.Model):
    title = models.CharField(max_length=300, null=False, verbose_name="عنوان")
    url = models.CharField(max_length=200, unique=True, verbose_name="لینک",default=True)
    # parent = models.ForeignKey("Talentcategory", null=True, blank=True, verbose_name="کلاس والد",
    #                            on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مهارتها"
        verbose_name_plural = "دسته بندی های مهارتها"
