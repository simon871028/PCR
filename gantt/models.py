from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=255)
    photo = models.URLField(
        default='https://www.csie.ntust.edu.tw/var/file/38/1038/pictures/654/m/mczh-tw1920x400_small74292_355196687813.jpg')


class Effect(models.Model):
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)
    skill_type = models.CharField(max_length=255)
    duration = models.FloatField()
    addtional_time = models.FloatField()
    description = models.CharField(max_length=255)
    is_weapon = models.BooleanField(max_length=255, default=False)
