from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
import django
# Create your models here.
class Person(AbstractUser):
    # email = models.EmailField(u'邮箱', null=False)
    name = models.CharField(u'姓名', max_length=20)
    nickname = models.CharField(u'昵称', max_length=10, default="")
    college = models.CharField(u'学院',max_length=10)
    IDnum = models.CharField(u'学号',max_length=10, unique=True)
    #---------------------------------------------------
    birthdate = models.CharField(null = True, blank = True, max_length = 20)
    major = models.CharField(null = True, blank = True, max_length = 50)
    loginkey = models.CharField(null=True, blank = True, max_length = 50)
    gender = models.IntegerField(null=True, blank=True, default=0)
    # user_info

class Community(models.Model):
    name = models.CharField(u'名字', max_length=20, primary_key=True)
    establish_date = models.DateField(u"创建时间", default=django.utils.timezone.now)
    introduction = models.CharField(u'简介', max_length=100, default="")
    #member = models.ManyToManyField(u'成员', Person)
    def __unicode__(self):
        return self.name

class Notice(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    community  = models.OneToOneField(Community)
    author = models.ManyToManyField(Person, related_name = "publish_notice")
    content = models.TextField(null=True, blank=True)
    create_time = models.DateField(null=True, blank = True)
    def __unicode__(self):
        return self.content
    def __str__(self):
        return self.content


class Passage(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    community  = models.OneToOneField(Community, default="")
    author = models.ManyToManyField(Person, related_name = "publish_psg")
    content = models.TextField(null=True, blank=True)
    create_time = models.DateField(null=True, blank = True)
    def __unicode__(self):
        return self.title


class Activity(models.Model):
    # hoster = models.ForeignKey(Association, on_delete=models.CASCADE)
    # community = models.ForeignKey(Community)
    community  = models.OneToOneField(Community)
    author = models.ManyToManyField(Person)
    name = models.CharField(null= True, blank = True, max_length = 200)
    # time = 2017.4.3 10:00 AM-11：30AM
    datetime = models.CharField(null=True, blank=True, max_length=200)
    address = models.CharField(null = True, blank = True, max_length = 200)
    introduction = models.CharField(null = True, blank = True, max_length=500)
    def __unicode__(self):
        return self.name


class ApplyFor(models.Model):
    community = models.ForeignKey(Community, related_name="applyfor", default=None)
    apply_time = models.DateField(null=True)


class Attend(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)


class Inform(models.Model):
    sender = models.ForeignKey(Person, default="")
    acceptor = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    # sendtime = models.

class MememberOf(models.Model):
    member = models.ForeignKey(Person, default="")
    community = models.ForeignKey(Community, default=None)
    role = models.CharField(null=True, blank=True, max_length=200)
    #访问控制权限,需要可以定制的,
    chair_privilege = {"update_community_info":True, "grant_level":1, "add_member":True, "delete_member":True,
                       "publish_passage":
                       True, "delete_passage":True}
    manager_privilege = {"update_community_info": False, "grant_level": 2, "add_member": True, "delete_member": True,
                         "publish_passage": True, "delete_passage": True}
    normal_privilege = {"update_community_info": False, "grant_level": 3, "add_member": False, "delete_member": False,
                         "publish_passage": True, "delete_passage": True}
    privilege = {"chair": chair_privilege, "manager":manager_privilege, "normal": normal_privilege}




'''class Person_Community:
    Perosn
    Community'''






# -----------------------------------------------------------------





