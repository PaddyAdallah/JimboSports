from django.db import models
from users.models import Officials, Team


# Create your models here.
# Leagues
class League(models.Model):
    db_table = 'league'
    official_id = models.ForeignKey(Officials, on_delete=models.DO_NOTHING)
    league_name = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.league_name


# Enroll teams to leagues
class LeagueTeam(models.Model):
    db_table = 'league_team'
    league_id = models.ForeignKey(League, on_delete=models.DO_NOTHING)
    team_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id



