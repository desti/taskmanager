# coding=utf-8

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from users.models import *

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    
admin.site.register(Company,CompanyAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','login_user','company')
    list_display_links = ('id','login_user')
    list_filter = ('company',)
    
admin.site.register(User,UserAdmin)

class UserSkillAdmin(admin.ModelAdmin):
    list_display = ('id','user','skill_level','current_points')
    list_display_links = ('id','user')
    list_filter = ('skill_level',)

admin.site.register(UserSkill,UserSkillAdmin)