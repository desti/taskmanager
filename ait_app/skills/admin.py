# coding=utf-8

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from skills.models import *

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    
admin.site.register(Skill,SkillAdmin)

class LevelAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    
admin.site.register(Level,LevelAdmin)

class SkillLevelAdmin(admin.ModelAdmin):
    list_display = ('id','skill','level','order')
    list_display_links = ('id','skill')
    
admin.site.register(SkillLevel,SkillLevelAdmin)