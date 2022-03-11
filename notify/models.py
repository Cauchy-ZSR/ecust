from tkinter import CASCADE
from django.db import models
from user.models import user
from forum.models import forum

# Create your models here.
class notice(models.Model):
    id = models.AutoField(verbose_name='通知编号', primary_key=True)
    content = models.TextField(verbose_name='通知内容')
    receiver = models.ForeignKey(user, verbose_name='通知接收人',related_name='通知接收人', on_delete=models.CASCADE)
    sender = models.ForeignKey(user, verbose_name='通知发布人', related_name='通知发送人', on_delete=models.CASCADE)
    range = models.ForeignKey(forum, verbose_name='发送范围', on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='发送时间', auto_now_add=True)
    is_read = models.BooleanField(verbose_name='是否已读', default=False)
    class Meta:
        db_table = 'notify_notice'
