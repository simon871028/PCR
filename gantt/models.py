from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=255)

class Skill(models.Model):
    name = models.CharField(max_length=255)
    character_id = models.ForeignKey(Character,on_delete =models.CASCADE)
    time_interval = models.FloatField(),
    addtional_time = models.FloatField(),
    skill_type = models.IntegerField()

class Timeline(models.Model):
    
