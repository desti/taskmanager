# coding=utf-8

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from tasks.models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','created_on','name','creator','worker','finished_percentage')
    list_display_links = ('id','created_on')

admin.site.register(Task,TaskAdmin)

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id','task','user','has_accepted')
    list_display_links = ('id','task')
    list_filter = ('has_accepted',)

admin.site.register(Candidate,CandidateAdmin)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')

admin.site.register(Status,StatusAdmin)

class StatusRuleAdmin(admin.ModelAdmin):
    list_display = ('id','from_status','to_status')
    list_display_links = ('id','from_status')
    
admin.site.register(StatusRule,StatusRuleAdmin)

class StatusLogAdmin(admin.ModelAdmin):
    list_display = ('id','created_on','task','status','subject')
    list_display_links = ('id','created_on')
    list_filter = ('created_on','status')
    
admin.site.register(StatusLog,StatusLogAdmin)