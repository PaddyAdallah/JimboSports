from django.db import models


# user profile
class UserProfile(models.Model):
    # user type choices
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'ref'),
        (3, 'coach'),
        (4, 'official')
    )

    userName = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, unique=True)
    image = models.ImageField(upload_to='images/%m/%d')
    gender = models.CharField(max_length=10)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return str(self.userName)


# Create your models here.
class Officials(models.Model):
    db_table = 'officials'
    official = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.official)


# referee table
class Referee(models.Model):
    db_table = 'referee'
    referee = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)
    status = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.referee)


# coach table
class Coach(models.Model):
    db_table = 'coach'
    coach = models.OneToOneField(UserProfile, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.coach)


# team table
class Team(models.Model):
    db_table = 'team'
    teams_name = models.CharField(max_length=40)
    team_image = models.ImageField(upload_to='teams')
    coach = models.ForeignKey(Coach, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.teams_name
