from django.db import models

from user_module.models import User


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
    author = models.ForeignKey(User,editable=False, null=True,blank=True, verbose_name="نویسنده", on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True, verbose_name="زمان انتشار")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = " مقاله"
        verbose_name_plural = "مقالات"

class Comments(models.Model):
    article =  models.ForeignKey("Article",on_delete=models.CASCADE,verbose_name="مقاله")
    author = models.ForeignKey(User ,  on_delete=models.CASCADE,verbose_name="نویسنده کامنت")
    parent = models.ForeignKey("Comments",null=True,blank=True,on_delete=models.CASCADE,verbose_name="والد")
    date_created = models.DateField(auto_now_add=True, verbose_name="زمان انتشار")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    text = models.TextField(verbose_name="متن")

    def __str__(self):
        return f"کامنت شماره{self.id}"

    class Meta:
        verbose_name = " کامنت"
        verbose_name_plural = "کامنت ها"