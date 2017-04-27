from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

from .forms import RegistForm, LoginForm
from .models import Person
# Create your views here.

def welcome(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method== 'POST':
        lf = LoginForm(request.POST)
        if lf.is_valid():
            _Username = lf.cleaned_data['username']
            _Password = lf.cleaned_data['password']
            user = auth.authenticate(username=_Username, password=_Password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('/home')
            else:
                return HttpResponse(u"用户或密码错误")
    else:
        lf = LoginForm()
    return render(request,'welcome.html', { 'lf':lf, })

def regist(request):
    if request.method == 'POST':

        rf = RegistForm(request.POST)

        if rf.is_valid():
            _Username = request.POST.get('username')
            _Email = request.POST.get('email')
            _Password = request.POST.get('password')
            _Password2 = request.POST.get('passwordagain')
            _College = request.POST.get('college')
            _IDnum = request.POST.get('IDnum')
            _Name = request.POST.get('name')
            if _Password != _Password2:
                return HttpResponse(u"两次密码不一致")
            Person.objects.create_user(username=_Username, email=_Email, password=_Password, college=_College, IDnum=_IDnum, name=_Name)
            return HttpResponse(u"注册成功")
    else:
        rf = RegistForm()
    return render(request,'regist.html', {'rf': rf, })


@login_required(login_url='/')
def home(request):
    user = request.user
    return render(request,'home.html', {'user': user, })

@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    return redirect('/')