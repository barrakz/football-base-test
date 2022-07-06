from django.contrib import admin
from .models import Player, Club, Match

admin.site.register(Club)
admin.site.register(Player)
admin.site.register(Match)
