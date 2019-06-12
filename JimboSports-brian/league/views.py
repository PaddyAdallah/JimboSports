from rest_framework import viewsets

from league import models
from . import serializers


# Create your views here.


class LeagueViewSet(viewsets.ModelViewSet):
    queryset = models.League.objects.all()
    serializer_class = serializers.LeagueSerializer


class LeagueTeamsViewSet(viewsets.ModelViewSet):
    queryset = models.LeagueTeam.objects.all()
    serializer_class = serializers.LeagueTeamSerializer
