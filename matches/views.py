from rest_framework import viewsets

from matches import models
from . import serializers


# Create your views here.


class MatchFixturesViewSet(viewsets.ModelViewSet):
    queryset = models.MatchFixtures.objects.all()
    serializer_class = serializers.MatchFixturesSerializer


class MatchResultsViewSet(viewsets.ModelViewSet):
    queryset = models.MatchResults.objects.all()
    serializer_class = serializers.MatchResultsSerializer
