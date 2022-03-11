from django.db import models

# Create your models here.

class userClass(models.Model):
    # 学院代码+年份+专业代码+班级数量
    class_id = models.CharField(verbose_name='班级编号', max_length=10, primary_key=True)
    institute = models.CharField(verbose_name='学院', max_length=32)
    className = models.CharField(verbose_name='班级名称', max_length=32)
    grade = models.CharField('年级', max_length=32)
    class Meta:
        db_table = 'user_class'


class user(models.Model):
    userNo = models.CharField(verbose_name='用户编号', max_length=8, primary_key=True)
    nickname = models.CharField(verbose_name='昵称', max_length=30)
    sex = models.BooleanField(verbose_name='性别', null=True)
    wx = models.CharField(verbose_name='微信号', max_length=32)
    email = models.EmailField(verbose_name='邮箱',null=True)
    intro = models.TextField(verbose_name='简介', default='')
    identity = models.CharField(verbose_name='身份', max_length=5)
    userIcon = models.ImageField(verbose_name='用户头像', upload_to='userIcon')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateField(auto_now=True)
    userClass = models.ForeignKey(userClass, on_delete=models.CASCADE)
    class Meta:
        db_table = 'user_user'
