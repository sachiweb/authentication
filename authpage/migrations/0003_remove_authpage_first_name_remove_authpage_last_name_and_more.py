# Generated by Django 4.1.5 on 2023-03-08 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authpage', '0002_authpage_first_name_authpage_last_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authpage',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='authpage',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='authpage',
            name='user_email',
        ),
    ]
