from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    activation_code = models.CharField(max_length=200, verbose_name='ایمیل فعال سازی')
    avatar = models.ImageField(verbose_name='آواتار',null=True)
    about = models.TextField(verbose_name="درباره شخص",null=True,blank=True)
    number =  models.IntegerField(blank=True,null=True,verbose_name="شماره همراه")
    class Meta:
        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'

    def __str__(self):
        if self.first_name is not  "" and self.last_name is not  "":
            return self.get_full_name()
        return self.email