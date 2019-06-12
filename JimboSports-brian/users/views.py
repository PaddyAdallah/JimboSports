from rest_framework import viewsets

from users import models
from . import serializers


class OfficialsViewSet(viewsets.ModelViewSet):
    queryset = models.Officials.objects.all()
    serializer_class = serializers.UserProfileSerializer


class RefereesViewSet(viewsets.ModelViewSet):
    queryset = models.Referee.objects.all()
    serializer_class = serializers.RefereesSerializers


class CoachesViewSet(viewsets.ModelViewSet):
    queryset = models.Coach.objects.all()
    serializer_class = serializers.CoachesSerializers


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer


class TeamsViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamsSerializer
