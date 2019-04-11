from django.db import models
from users.models import Referee, Team
from league.models import League


# Create your models here.
# match fixtures
class MatchFixtures(models.Model):
    db_table = 'match_fixtures'
    match_date = models.DateField()
    team1_id = models.ForeignKey(Team, related_name='team1', on_delete=models.DO_NOTHING)
    team2_id = models.ForeignKey(Team, related_name='team2', on_delete=models.DO_NOTHING)
    league_id = models.ForeignKey(League, on_delete=models.DO_NOTHING)
    referee_id = models.ForeignKey(Referee, on_delete=models.DO_NOTHING)
    venue = models.CharField(max_length=30)
    comments = models.CharField(max_length=255)

    def __str__(self):
        return self.id


# match results
class MatchResults(models.Model):
    db_table = 'match_results'
    ref_id = models.ForeignKey(Referee, on_delete=models.DO_NOTHING)
    match_fixture_id = models.ForeignKey(MatchFixtures, on_delete=models.DO_NOTHING)
    scores = models.IntegerField()
    points = models.IntegerField()
    team_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    league_id = models.ForeignKey(League, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.scores

