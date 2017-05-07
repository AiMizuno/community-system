from django import forms
from .models import Person, Inform

college_choice = (
    ('SDCS', u"数据科学与计算机学院"),
    ('ABC', u"电信学院"),
    ('BCD', u"管理学院"),
)


class RegistForm(forms.ModelForm):
    college = forms.ChoiceField(label=u"学院", required=True, choices=college_choice)
    password = forms.CharField(label=u"密码", required=True, widget= forms.PasswordInput())
    passwordagain = forms.CharField(label=u"确认密码", required=True, widget=forms.PasswordInput())
    username = forms.CharField(label=u"账号", required=True, )
    email = forms.EmailField(label=u"邮箱", required=True,)
    class Meta:
        model = Person
        fields = ['username', 'name', 'password', 'passwordagain', 'IDnum', 'college', 'email',]
        #fields = ['username', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(label=u'账号', required=True, max_length=30)
    password = forms.CharField(label=u'密码',required=True,widget=forms.PasswordInput(), max_length=20)


actv = (
    ('SDCS', u"数据科学与计算机学院"),
    ('ABC', u"电信学院"),
    ('BCD', u"管理学院"),
)


class NewActivityForm(forms.Form):
    username = forms.CharField(label=u'作者',  required=True, max_length=60)
    hoster = forms.CharField(label=u'发起社团', required=True, max_length=60)
    name = forms.CharField(label=u'名称', max_length=200)
    introduction = forms.CharField(label=u'介绍', max_length=200)
    #introduction = forms.Textarea()
    datetime = forms.CharField(label=u'活动时间', required=True, max_length=60)
    address = forms.CharField(label=u'活动场地', required=True,  max_length=200)


class InformTable(forms.Form):
    sender = forms.CharField(label=u'发送人', required=True, max_length=60)
    acceptor = forms.CharField(label=u'收信人', required=True, max_length=60)
    content = forms.CharField(label=u'内容', required=True, max_length=200)
    class Meta():
        model = Inform
        fields = ['sender', 'acceptor','content']