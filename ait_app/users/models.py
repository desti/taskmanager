# coding=utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User as DjangoUser

from ait_app.skills.models import SkillLevel


class Company(models.Model):
    name = models.CharField(_('Name'),max_length=256)
    
    class Meta:
        verbose_name = _('Firma')
        verbose_name_plural = _('Firmen')
        ordering = ('name',)
    
    def __unicode__(self):
        return self.name


class User(models.Model):
    
    login_user = models.ForeignKey(DjangoUser,verbose_name=_('Login User'))
    company = models.ForeignKey(Company,verbose_name=_('Firma'))
    
    class Meta:
        verbose_name = _('Benutzer')
        verbose_name_plural = _('Benutzer')
    
    def __unicode__(self):
        return u"%s %s" % (self.login_user.first_name,self.login_user.last_name)


class UserSkill(models.Model):
    user = models.ForeignKey(User,verbose_name=_('Benutzer'))
    skill_level = models.ForeignKey(SkillLevel,verbose_name=_(u'Fähigkeitslevel'))
    current_points = models.IntegerField(default=0) 
    
    class Meta:
        verbose_name = _(u'Benutzerfähigkeit')
        verbose_name_plural = _(u'Benutzerfähigkeiten')
        unique_together = (("user", "skill_level"),)
    
    def __unicode__(self):
        return u"%s (%s)" % (self.skill_level, self.current_points)