# Generated by Django 2.1.7 on 2019-03-23 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户扩展信息'},
        ),
    ]
