from django.contrib import admin
# Register your models here.
from players.models import Players, Participation, PlayersStats, Transfers

admin.site.register(Players)
admin.site.register(Participation)
admin.site.register(PlayersStats)
admin.site.register(Transfers)
