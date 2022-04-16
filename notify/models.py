from django.db import models
from user.models import user
from forum.models import forum

# Create your models here.
class pub_notice(models.Model):
    id = models.AutoField(verbose_name='通知编号', primary_key=True)
    title = models.CharField(verbose_name='通知标题', max_length=32)
    content = models.TextField(verbose_name='通知内容')
    sender = models.ForeignKey(user, verbose_name='通知发布人', related_name='通知发送人', on_delete=models.CASCADE)
    range = models.ForeignKey(forum, verbose_name='发送范围', on_delete=models.CASCADE)
    created_time = models.DateTimeField(verbose_name='发送时间', auto_now_add=True)
    class Meta:
        db_table = 'notify_pub_notice'

class notice_receive(models.Model):
    notice = models.ForeignKey(pub_notice, on_delete=models.CASCADE, verbose_name='通知编号')
    receiver = models.ForeignKey(user, on_delete=models.CASCADE, verbose_name='接收人')
    is_read = models.BooleanField(verbose_name='是否已读', default=False)
    class Meta:
        db_table = 'notify_notice_receive'