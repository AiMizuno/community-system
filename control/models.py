from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Person(AbstractUser):
    email = models.EmailField(u'邮箱', null=False)
    name = models.CharField(u'昵称', max_length=10)
    college = models.CharField(u'学院',max_length=10)
    IDnum = models.CharField(u'学号',max_length=10, unique=True)
    #join = models.ManyToManyField(u'参加社团',Community)

class Community(models.Model):
    name = models.CharField(u'名字', max_length=20, primary_key=True)
    #member = models.ManyToManyField(u'成员', Person)

'''class Person_Community:
    Perosn
    Community'''