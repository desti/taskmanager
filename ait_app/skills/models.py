from django.db import models

class Skill(models.Model):
    """
    Skill
    """
    
    name = models.CharField(unique=True)
    
class Level(models.Model):
    """
    Level: describes a distinct stage of a skill
    """
    
    name = models.CharField(unique=True)
    
class SkillLevel(models.Model):
    """
    describes the mapping of all possible levels of a skill 
    """
    
    skill = models.ForeignKey(Skill)
    level = models.ForeignKey(Level)
    order = models.IntegerField() 
    
    class Meta:
        unique_together = (("skill", "level"), ("skill", "order"), )