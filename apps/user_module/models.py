from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.teacher_module.models import TalentCategory
# from sorl.thumbnail import ImageField, get_thumbnail
from PIL import Image

# Create your models here.
class User(AbstractUser):
    activation_code = models.CharField(max_length=200, verbose_name='ایمیل فعال سازی')
    about = models.TextField(verbose_name="درباره شخص",null=True,blank=True)

    number =  models.IntegerField(blank=True,null=True,verbose_name="شماره همراه")

    talent=models.ManyToManyField(TalentCategory,blank=False,verbose_name="مهارت یا دسته بندی مورد علاقه ")
    avatar = models.ImageField(verbose_name='آواتار',null=True,blank=True,upload_to="User-avatar",)
    

    class Meta:

        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'

    def __str__(self):
        if self.first_name is not  "" and self.last_name is not  "":
            return self.get_full_name()
        return self.email
    
    # def save(self):
    #     super().save()  # saving image first

    #     img = Image.open(self.avatar.path) # Open image using self

    #     if img.height > 150 or img.width > 150:
    #         new_img = (150, 150)
    #         img.thumbnail(new_img)
    #         img.save(self.avatar.path)