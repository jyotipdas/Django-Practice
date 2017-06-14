# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import UserProfile
# Register your models here.



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_info', 'phone_no','city','website')

    def user_name(self,obj):
        return obj.user

    def user_info(self,obj):
        return obj.description

    def phone_no(self,obj):
        return obj.phone

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin,self).get_queryset(request)
        queryset = queryset.order_by('-phone','user')
        return queryset

    user_info.short_description = 'INFO'

admin.site.register(UserProfile,UserProfileAdmin)
