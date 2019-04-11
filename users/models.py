from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Officials (models.Model):
    db_table = 'officials'
    name = models.CharField(max_length=30)
    uname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    image = models.CharField(max_length=100)
    category = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Referee (models.Model):
    db_table = 'referee'
    ref_name = models.CharField(max_length=100)
    uname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    image = models.CharField(max_length=100)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.ref_name


class Team (models.Model):
    db_table = 'team'
    team_name = models.CharField(max_length=40)
    gender = models.CharField(max_length=10)
    uname = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    image = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)
    constituency = models.CharField(max_length=30)

    def __str__(self):
        return self.team_name

