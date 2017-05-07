"""community_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from control import views as control_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', control_views.logout, name='logout'),
    url(r'^register/$', control_views.register, name="register"),
    url(r'^home/$', control_views.home, name="home"),
    url(r'^$', control_views.welcome, name="welcome"),
    url(r'^infos$', control_views.selfinfo, name="selfinfo"),
    # 社团活动, 主页
    url(r'^affairs$', control_views.affairs, name='affairs'),
    url(r'homepage$', control_views.homepage, 'homepage'),
    url(r'^create_activity$', control_views.create_activity, name="create_activity"),
    url(r'^create_activity/(.{3})$', control_views.create_activity, name="create_activity"),
    url(r'^get_user/?$', control_views.get_user, name="get_user"),
    #通知
    url(r'^send_inform/([0-9a-zA-Z]+)/?$', control_views.send_inform, name="send_inform"),
    url(r'^send_inform/?$', control_views.send_inform, name="send_inform"),
    url(r'^watch_inform/?$', control_views.watch_inform, name="watch_inform"),
    url('^activity/?$', control_views.watch_activity),
    url('^attend_activity/(.*?)/?$', control_views.attend_activity),
]
