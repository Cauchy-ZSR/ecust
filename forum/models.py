from distutils.command.upload import upload
from django.db import models
from user.models import user
# Create your models here.


class forum(models.Model):
    id = models.AutoField(verbose_name='论坛编号', primary_key=True)
    name = models.CharField(verbose_name='论坛名称', max_length=32, unique=True)
    creater = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='创建者')
    forumIcon = models.ImageField(verbose_name='论坛头像', upload_to='forumIcon')
    intro = models.TextField(verbose_name='简介', default='')
    tag = models.CharField(verbose_name='标签', max_length=32)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    class Meta:
        db_table = 'forum_forum'


class topic(models.Model):
    id = models.AutoField(verbose_name='帖子编号', primary_key=True)
    creater = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='创建者')
    pubForum = models.ForeignKey(forum, on_delete=models.CASCADE, verbose_name='创建论坛')
    title = models.CharField(verbose_name='标题', max_length=32)
    content = models.TextField(verbose_name='内容')
    created_time = models.DateTimeField(verbose_name='创贴时间', auto_now_add=True)
    tag = models.CharField(verbose_name='帖子分类', max_length=32)
    class Meta:
        db_table = 'forum_topic'


class comment(models.Model):
    id = models.AutoField(verbose_name='评论编号', primary_key=True)
    puber = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='评论人')
    created_time = models.DateTimeField(verbose_name='评论时间', auto_now_add=True)
    topicComment = models.ForeignKey(topic, on_delete=models.CASCADE, verbose_name='评论对象')
    is_read = models.BooleanField(verbose_name='是否已读', default=False)
    class Meta:
        db_table='forum_comment'


class membership(models.Model):
    m_forum = models.ForeignKey(forum, on_delete=models.CASCADE, verbose_name='论坛')
    m_user = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='论坛成员')
    is_admin = models.BooleanField(verbose_name='是否为管理员', default=False)
    class Meta:
        db_table='forum_user'