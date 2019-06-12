from rest_framework import viewsets

from players import models
from . import serializers


class PlayersViewSet(viewsets.ModelViewSet):
    queryset = models.Players.objects.all()
    serializer_class = serializers.PlayersSerializer


class PlayerStatsViewSet(viewsets.ModelViewSet):
    queryset = models.PlayersStats.objects.all()
    serializer_class = serializers.PlayersStats


class TransfersViewSet(viewsets.ModelViewSet):
    queryset = models.Transfers.objects.all()
    serializer_class = serializers.Transfers


class ParticipationViewSet(viewsets.ModelViewSet):
    queryset = models.Participation.objects.all()
    serializer_class = serializers.Participation
