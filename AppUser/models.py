from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile_user')
    SEX_CHOICES = (
        (u'M', u"男性-Male"),
        (u'F', u"女性-Female"),
    )
    sex = models.CharField(max_length=2, verbose_name="性别", choices=SEX_CHOICES)
    age = models.IntegerField(verbose_name="年龄")
    birthday = models.DateField(verbose_name=u'生日', blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name=u'地址', blank=True, default=u'无')
    # head_portrait = models.ImageField(upload_to='images/%Y/%m', verbose_name=u'头像')
    telephone = models.CharField(max_length=50, blank=True, default=u'无')

    class Meta:
        db_table = 't_user_profile'

    def __str__(self):
        return self.user
