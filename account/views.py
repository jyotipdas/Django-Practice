# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def home(request):
    return render(request,'account/home.html')

def register(request):
    if request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = forms.RegistrationForm()
        args = {'form':form}
        return render(request,'account/reg_form.html',args)


def view_profile(request):
    args={'user':request.user}
    return render(request,'account/profile.html',args)

def edit_profile(request):
    if request.method == 'POST':
        form = forms.EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = forms.EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'account/edit_profile.html',args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'account/change_password.html', args)
