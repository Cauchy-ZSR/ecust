from django.db import models

# Create your models here.


class user(models.Model):
    userNo = models.CharField(verbose_name='用户编号', max_length=8, primary_key=True)
    password = models.CharField(verbose_name='密码', max_length=32)
    nickname = models.CharField(verbose_name='昵称', max_length=30, null=True)
    sex = models.CharField(verbose_name='性别', max_length=1, null=True)
    email = models.EmailField(verbose_name='邮箱',null=True)
    identity = models.CharField(verbose_name='身份', max_length=5, null=True)
    userIcon = models.TextField(verbose_name='用户头像', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    class Meta:
        db_table = 'user_user'
