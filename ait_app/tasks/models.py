# coding=utf-8

from django.utils.translation import ugettext_lazy as _
from django.db import models
from ait_app.skills.models import SkillLevel
from ait_app.users.models import User

class Task(models.Model):
    name = models.CharField(_('Name'),max_length=256)
    description = models.TextField(_('Beschreibung'),blank=True,null=True)
    created_on = models.DateTimeField(_('Erstellt am'),auto_now_add=True)
    updated_on = models.DateTimeField(_('Zuletzt gespeichert'),auto_now=True)
    creator = models.ForeignKey(User,related_name='created_tasks',verbose_name=_('Ersteller'))
    worker = models.ForeignKey(User, related_name='worker_tasks',verbose_name=_('Arbeiter'), null=True,blank=True)
    
    finished_percentage = models.FloatField(default=0.0)
    
    parent = models.ForeignKey('self', related_name='child_set', null=True, blank=True)
    
    required_skills = models.ManyToManyField(SkillLevel,verbose_name=_(u'Benötigte Skills'),blank=True)
    candidates = models.ManyToManyField(User,through='Candidate')
    
    class Meta:
        verbose_name = _('Aufgabe')
        verbose_name_plural = _('Aufgaben')
    
    def __unicode__(self):
        return self.name

class Candidate(models.Model):
    task = models.ForeignKey(Task,verbose_name=_('Aufgabe'))
    user = models.ForeignKey(User,verbose_name=_('Benutzer'))
    has_accepted = models.BooleanField(_('Hat akzeptiert'),default=False)
    
    class Meta:
        verbose_name = _('Kandidat')
        verbose_name_plural = _('Kandidaten')
        unique_together = (("task", "user"),)
    
    def __unicode__(self):
        return u"%s %s" % (self.task, self.user)

    
class Status(models.Model):
    name = models.CharField(_('Name'),max_length=32, unique=True)
    
    class Meta:
        verbose_name = _('Status')
        verbose_name_plural = _('Status')
    
    def __unicode__(self):
        return self.name
    
    
class StatusRule(models.Model):
    from_status = models.ForeignKey(Status,verbose_name=_('Ausgangsstatus'),related_name='from_rules')
    to_status = models.ForeignKey(Status,verbose_name=_('Zielstatus'),related_name='to_rules')
    
    class Meta:
        verbose_name = _(u'Statusregel')
        verbose_name_plural = _(u'Statusregeln')
        unique_together = (("from_status", "to_status"),)
    
class StatusLog(models.Model):
    task = models.ForeignKey(Task,verbose_name=_('Aufgabe'))
    status = models.ForeignKey(Status,verbose_name=_('Status'))
    created_on = models.DateTimeField(_('Erstellt am'),auto_now_add=True)
    created_by = models.ForeignKey(User,verbose_name=_('Erstellt von'),null=True,blank=True)
    subject = models.CharField(_('Betreff'),max_length=512)
    message = models.TextField(_('Nachricht'),blank=True,null=True)
    
    class Meta:
        verbose_name = _('Status Log')
        verbose_name_plural = _('Status Logs')
        ordering = ('-created_on',)
    
    def __unicode__(self):
        return self.subject
        