from django.contrib import admin

# Register your models here.
from users.models import UserProfile, Referee, Team, Officials

admin.site.register(Referee)
admin.site.register(UserProfile)
admin.site.register(Team)
admin.site.register(Officials)
