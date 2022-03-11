# Generated by Django 4.0 on 2022-03-11 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userClass',
            fields=[
                ('class_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='班级编号')),
                ('institute', models.CharField(max_length=32, verbose_name='学院')),
                ('className', models.CharField(max_length=32, verbose_name='班级名称')),
                ('grade', models.CharField(max_length=32, verbose_name='年级')),
            ],
            options={
                'db_table': 'user_class',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('userNo', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='用户编号')),
                ('nickname', models.CharField(max_length=30, verbose_name='昵称')),
                ('sex', models.BooleanField(null=True, verbose_name='性别')),
                ('wx', models.CharField(max_length=32, verbose_name='微信号')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('intro', models.TextField(default='', verbose_name='简介')),
                ('identity', models.CharField(max_length=5, verbose_name='身份')),
                ('userIcon', models.ImageField(upload_to='userIcon', verbose_name='用户头像')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateField(auto_now=True)),
                ('userClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userclass')),
            ],
            options={
                'db_table': 'user_user',
            },
        ),
    ]
