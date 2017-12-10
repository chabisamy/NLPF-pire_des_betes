"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from mysite.core import views as core_views
from mysite.projects import views as project_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^$', project_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^new_project/$', project_views.new_project, name='new_project'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^project/(?P<pk>[-\w]+)/$', project_views.project_details, name='project_details'),
    url(r'^project/(?P<pk>[-\w]+)/add_counterpart/$', project_views.add_counterpart, name='add_counterpart'),
]
