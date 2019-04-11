from django.contrib import admin

# Register your models here.
from matches.models import MatchFixtures, MatchResults

admin.site.register(MatchFixtures)
admin.site.register(MatchResults)
