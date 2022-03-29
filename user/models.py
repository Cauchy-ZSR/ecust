from django.db import models

# Create your models here.


class user(models.Model):
    userNo = models.CharField(verbose_name='用户编号', max_length=8, primary_key=True)
    nickname = models.CharField(verbose_name='昵称', max_length=30)
    sex = models.BooleanField(verbose_name='性别', null=True)
    email = models.EmailField(verbose_name='邮箱',null=True)
    identity = models.CharField(verbose_name='身份', max_length=5)
    userIcon = models.ImageField(verbose_name='用户头像', upload_to='userIcon')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    class Meta:
        db_table = 'user_user'
