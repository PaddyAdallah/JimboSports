from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Officials (models.Model):
    db_table = 'officials'
    official = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.official_user_name)


# referee table
class Referee (models.Model):
    db_table = 'referee'
    ref = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.ref_user_name)


# coach table
class Coach(models.Model):
    db_table = 'coach'
    coach = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.coach_user_name)


# team table
class Team (models.Model):
    db_table = 'team'
    coach = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    team_name = models.CharField(max_length=40)
    team_image = models.ImageField(upload_to='teams')
    constituency = models.CharField(max_length=30)

    def __str__(self):
        return self.team_name


# user profile
class UserProfile(models.Model):
    # user type choices
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'ref'),
        (3, 'coach'),
        (4, 'official')
    )

    user = models.OneToOneField(User, unique=True, on_delete=models.DO_NOTHING)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30, unique=True)
    image = models.ImageField(upload_to='images/%m/%d')
    gender = models.CharField(max_length=10)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def __str__(self):
        return str(self.user)
