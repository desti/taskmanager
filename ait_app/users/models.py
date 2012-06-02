from django.db import models
from ait_app.skills.models import SkillLevel

class User(models.Model):
    """
    User
    """
    
    logon = models.CharField()
    name = models.CharField()
    password = models.CharField()
    email = models.EmailField(unique=True)
    

class UserSkill(models.Model):
    """
    Mapping of the skills according to a user
    """    
    
    user = models.ForeignKey(User)
    skill_level = models.ForeignKey(SkillLevel)
    
    class Meta:
        unique_together = (("user", "skill_level"), )
    