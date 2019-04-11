from django.db import models
from users.models import Team
from matches.models import MatchFixtures
# Create your models here.


# players information
class Players(models.Model):
    db_table = 'players'
    photo = models.ImageField(upload_to='players/%m/%d')
    birth_certificate = models.ImageField(upload_to='birth/%m/%d')
    current_team_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    date_joined = models.DateField()
    date_left = models.DateField()
    player_status = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    position = models.CharField(max_length=30)
    sub_team = models.CharField(max_length=2)

    def __str__(self):
        return self.name


# player statics
class PlayersStats(models.Model):
    db_table = 'player_stats'
    match_fixture_id = models.ForeignKey(MatchFixtures, on_delete=models.DO_NOTHING)
    player_id = models.ForeignKey(Players, on_delete=models.DO_NOTHING)
    team_id = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    goals = models.IntegerField()
    match_time = models.DateField()
    injured = models.CharField(max_length=5)
    cards = models.CharField(max_length=5)

    def __str__(self):
        return self.player_id


# transfers
class Transfers(models.Model):
    db_table = 'transfers'
    player_id = models.ForeignKey(Players, on_delete=models.DO_NOTHING)
    from_team_id = models.ForeignKey(Team, related_name='from_team_name', on_delete=models.DO_NOTHING)
    start_date = models.DateField()
    end_date = models.DateField()
    to_team_id = models.ForeignKey(Team, related_name='to_team_Name', on_delete=models.DO_NOTHING)
    additional_info = models.TextField()

    def __str__(self):
        return self.id


# store each player who participated
class Participation(models.Model):
    db_table = 'participation'
    player_id = models.ForeignKey(Players, on_delete=models.DO_NOTHING)
    game_id = models.ForeignKey(MatchFixtures, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id

