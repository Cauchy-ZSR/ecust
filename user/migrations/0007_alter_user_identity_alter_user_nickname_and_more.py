# Generated by Django 4.0 on 2022-04-15 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='identity',
            field=models.CharField(max_length=5, null=True, verbose_name='身份'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=30, null=True, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userIcon',
            field=models.TextField(null=True, verbose_name='用户头像'),
        ),
    ]