from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=40)
    isDelete = models.BooleanField(default=False)


class AreaInfo(models.Model):
    code = models.IntegerField(max_length=10)
    name = models.CharField(max_length=32)
    parent_id = models.IntegerField(max_length=11)
    level_id = models.CharField(max_length=32)
    class Meta:
        db_table = 'sys_region'


class Test1(models.Model):
    content = HTMLField()