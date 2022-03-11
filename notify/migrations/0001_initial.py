# Generated by Django 4.0 on 2022-03-11 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('forum', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='通知编号')),
                ('content', models.TextField(verbose_name='通知内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='发送时间')),
                ('range', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum', verbose_name='发送范围')),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='通知接收人', to='user.user', verbose_name='通知接收人')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='通知发送人', to='user.user', verbose_name='通知发布人')),
            ],
            options={
                'db_table': 'notify_notice',
            },
        ),
    ]
