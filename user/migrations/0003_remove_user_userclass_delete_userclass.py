# Generated by Django 4.0 on 2022-03-29 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userClass',
        ),
        migrations.DeleteModel(
            name='userClass',
        ),
    ]
