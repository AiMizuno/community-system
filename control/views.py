from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from .forms import RegistForm, LoginForm, NewActivityForm
from .models import Person
from .models import Activity, Community, Inform, Attend
from django.template import RequestContext
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


def register(request):
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


def selfinfo(request):
    user = request.user
    return render(request, 'selfinfo.html', {'user':user})


@login_required(login_url='/')
def home(request):
    user = request.user
    response = render_to_response('home.html', {'user':user})
    response.set_cookie('username', user)
    # return render(request, 'home.html', {'user': user})
    return response

@login_required(login_url="/")
def logout(request):
    auth.logout(request)
    return redirect('/')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def affairs(request):
    #dic = dict(), dic[activity], dic[username], dic[]
    return render(request, 'affairs.html')


def homepage(request):
    return render(request, 'homepage.html')


def create_activity(request, info = 'no'):
    if info == 'add':
        act_name = request.POST.get('name')
        #根据cookie而非POST数据
        username = request.COOKIES.get('username')
        hoster = request.POST.get('hoster')
        datetime = request.POST.get('datetime')
        address = request.POST.get('address')
        introduction = request.POST.get('introduction')

        cmt = Community.objects.get(name=hoster)
        author = Person.objects.get(name=username)
        # if community is existing
        if cmt:
            newact = Activity.objects.get_or_create(community=cmt)[0] # 返回(object, False)
            # save new activity
            if author:
                newact.author.add(author)
            # add other info
            newact.name = act_name
            newact.address = address
            newact.datetime = datetime
            newact.introduction = introduction
            newact.save()
            return HttpResponse(u'添加成功')
        else:
            return HttpResponse(u'社团不存在')
    else:
        form = NewActivityForm(request.POST)
    return render(request, 'create_activity.html', {'form': form})


# _activity -> attend -> watch what I attend
def watch_activity(request): #在主页获取
    dic = {}
    atys = Activity.objects.all()
    dic['activities'] = atys
    return render(request, '_activity.html', dic)


def attend_activity(request, atyname):
    username = request.user
    #
    user = Person.objects.filter(name=username)
    activity = Activity.objects.filter(name=atyname)
    if user:
        user = user[0]
    if activity:
        activity = activity[0]
    else:
        return HttpResponse('Not exist such an activity')
    attend = Attend(activity = activity, user=user)
    attend.save()
    return HttpResponse('attend success')

from .forms import InformTable
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_user(request): #看小伙伴
    userlist = Person.objects.all()
    dic = {'userlist': userlist}
    # watch userlist, which is made of name and its info
    return render(request, 'user.html', dic)

def send_inform(request, acceptor=None): #成员/发通知
    dic = {}
    if acceptor:
        # if it is the first time, a message is waiting to be finished
        username = request.COOKIES.get('username')
        acc = Person.objects.get(IDnum=acceptor)
        form = InformTable()
        dic['form'], dic['acceptor'] = form, acc
        return render(request, 'send_inform.html', dic)
    # the second time, add an inform to the database
    elif request.method == 'POST':
        inform = InformTable(request.POST)
        if inform.is_valid():
            username = inform.cleaned_data["sender"]
            sender = Person.objects.get(name=username)
            content = inform.cleaned_data["content"]
            acceptor = inform.cleaned_data["acceptor"]
            acc = Person.objects.get(IDnum=acceptor)
            newinform = Inform.objects.get_or_create(sender=sender, acceptor=acc, content=content)[0]
            newinform.save()
            return redirect('/watch_inform')
        else:
            return HttpResponse('Invalid POST')
    return HttpResponse('Method isn\'t POST')


def watch_inform(request):#导航栏的消息
    username = request.user
    user = Person.objects.get(name=username)
    dic = {}
    # 我发出的inform和我收到的inform
    if user:
        get_informs = Inform.objects.filter(acceptor=user)
        send_informs = Inform.objects.filter(sender=user)
        dic['gets'] = get_informs
        dic['sends'] = send_informs
        return render(request, 'informs.html', dic)
    return HttpResponse('Error')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def remove_activity(activity_id):
    Activity.objects.remove(activity_id=activity_id)


def remove_inform(community_id):
    Inform.objects.remove(community_id=community_id)

#这是测试的内容
def console(request):
    return render(request, 'console.html')
def console_activity(request):
    return render(request, 'console_activity.html')
def console_article(request):
    return render(request, 'console_article.html')
def console_inform(request):
    return render(request, 'console_inform.html')
def console_member(request):
    return render(request, 'console_member.html')