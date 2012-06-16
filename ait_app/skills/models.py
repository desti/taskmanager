# coding=utf-8

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Skill(models.Model):
    name = models.CharField(_('Name'),unique=True,max_length=256)
    
    class Meta:
        verbose_name = _(u'Fähigkeit')
        verbose_name_plural = _(u'Fähigkeiten')
        ordering = ('name',)
        
    def __unicode__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(_('Name'),unique=True,max_length=256)
    
    class Meta:
        verbose_name = _('Level')
        verbose_name_plural = _('Levels')
        ordering = ('name',)
        
    def __unicode__(self):
        return self.name


class SkillLevel(models.Model):
    skill = models.ForeignKey(Skill,verbose_name=_(u'Fähigkeit'))
    level = models.ForeignKey(Level,verbose_name=_(u'Level'))
    order = models.IntegerField(_('Reihenfolge'),default=0) 
    
    class Meta:
        verbose_name = _(u'Fähigkeitslevel')
        verbose_name_plural = _(u'Fähigkeitslevel')
        unique_together = (("skill", "level"), ("skill", "order"), )
        ordering = ('skill','order')
        
    def __unicode__(self):
        return "%s %s" % (self.skill, self.level)