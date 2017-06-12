# -*- coding: utf-8 -*-
# encoding: utf-8

"""MySite URL Configuration

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

from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done,password_reset_confirm
)

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login/$', login, {'template_name': 'account/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'account/logout.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$',password_reset,name='reset_password'),
    url(r'^reset-password/done/$',password_reset_done,name='password_reset_done'),
    url(r"^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\]+)/(?P<token>[0-9A-Za-z]{1,13}[0-9A-Za-z]{1,20})﻿/$",
        password_reset_confirm, name='password_reset_confirm'),
]
