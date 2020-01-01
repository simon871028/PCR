from django.contrib import admin

from .models import Character, Effect, TimeLine

admin.site.register(Character)
admin.site.register(Effect)
admin.site.register(TimeLine)