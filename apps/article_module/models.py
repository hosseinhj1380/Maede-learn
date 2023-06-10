from django.db import models
from apps.user_module.models import User


# Create your models here.

class ArticleCategory(models.Model):
    title = models.CharField(max_length=300, null=False, verbose_name="عنوان")
    url = models.CharField(max_length=200, unique=True, verbose_name="لینک")
    parent = models.ForeignKey("ArticleCategory", null=True, blank=True, verbose_name="کلاس والد",
                               on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دسته بندی مقالات"
        verbose_name_plural = "دسته بندی های مقالات"


class Article(models.Model):
    title = models.CharField(max_length=300, null=False, verbose_name="عنوان")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="عنوان در URL")
    selected_categories = models.ManyToManyField("ArticleCategory",verbose_name="دسته بندی ها ")
    short_description = models.CharField(max_length=300,verbose_name="توضیحات کوتاه")
    text = models.TextField(verbose_name="متن")
    image = models.ImageField(upload_to="article-images")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    comment=models.ForeignKey('Comments',null=True,blank=True,on_delete=models.CASCADE,verbose_name='کامنت ها ')
    writer=models.ForeignKey(User,verbose_name="نام نویسنده ",on_delete=models.CASCADE)
    date=models.DateField(null=False, blank=False, auto_now=True,verbose_name="تاریخ مقاله")
    

    # writer=models.CharField(max_length=255,null=False,verbose_name="نام و نام خانوادگی نویسنده ",default=None)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = " مقاله"
        verbose_name_plural = "مقالات"

class Comments (models.Model):
    blog=models.ForeignKey(Article,null=True,blank=True,on_delete=models.CASCADE,verbose_name='مقاله مربوطه  ')
    full_name = models.CharField(max_length=50,null=False,verbose_name='نام ')
    email = models.EmailField(verbose_name='ایمیل')
    message = models.TextField(max_length=500,null=False,verbose_name='پیام ')

    # title = models.ForeignKey(ArticleCategory,null=False,blank=False,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = " کامنت"
        verbose_name_plural = "کامنت ها"
