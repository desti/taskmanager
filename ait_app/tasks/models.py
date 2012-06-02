from django.db import models
from ait_app.skills.models import SkillLevel
from ait_app.users.models import User

class Task(models.Model):
    """
    Task
    """
    
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=4000)
    client = models.ForeignKey(User)
    responsible_person = models.ForeignKey(User, null=True)    
    
    finished_percentage = models.DecimalField(default=0)
    
    parentTask = models.ForeignKey(Task, null=True)

    
class TaskSkill(models.Model):
    """
    mapping of required skills for the given task
    """
    task = models.ForeignKey(Task)
    skill_level = models.ForeignKey(SkillLevel)
    
    class Meta:
        unique_together = (("task", "skill_level"), )
    
class AppropriateUser(models.Model):
    """
    mapping of possible responsible persons to solve a task
    """
    
    task = models.ForeignKey(Task)
    user = models.ForeignKey(User)
    has_accepted = models.BooleanField(default=False)
    
    class Meta:
        unique_together = (("task", "user"), )
    
class Status(models.Model):
    """
    Status of the work flow
    """
    
    name = models.CharField(max_length=32, unique=True)
    
    
class StatusRule(models.Model):
    """
    allowed changes of a status
    """

    from_status = models.ForeignKey(Status)
    to_status = models.ForeignKey(Status)
    
    class Meta:
        unique_together = (("from_status", "to_status"), )
    
class StatusLog(models.Model):
    """
    changes of the status of a task
    """
    
    task = models.ForeignKey(Task)
    status = models.ForeignKey(Status)
    insert_timestamp = models.DateTimeField()
    message = models.CharField(max_length=4000, null=True)
    
    class Meta:
        unique_together = (("task", "insert_timestamp"), )