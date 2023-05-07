from django.db import models


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = " مقاله"
        verbose_name_plural = "مقالات"

class Comments (models.Model):
    blog=models.ForeignKey(Article,null=True,blank=True,on_delete=models.CASCADE,verbose_name='بلاگ مربوطه ')
    full_name = models.CharField(max_length=50,null=False,verbose_name='نام ',default='hossein')
    email = models.EmailField(verbose_name='ایمیل',default='hossein@hossein.com')
    message = models.CharField(max_length=500,null=False,verbose_name='پیام ',default='nothing')

    # title = models.ForeignKey(ArticleCategory,null=False,blank=False,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.full_name