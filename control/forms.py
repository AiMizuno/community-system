from django import forms
from .models import Person

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
    class Meta:
        model = Person
        fields = ['username', 'name', 'password', 'passwordagain', 'IDnum', 'college', 'email',]
        #fields = ['username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(label=u'账号', required=True, max_length=30)
    password = forms.CharField(label=u'密码',required=True,widget=forms.PasswordInput(), max_length=20)