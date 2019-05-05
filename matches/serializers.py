from rest_framework import serializers

from .models import MatchFixtures, MatchResults


# create serializers
class MatchFixturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchFixtures
        fields = '__all__'
        # exclude = ('users',)
        # to exclude any unwanted fields


class MatchResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchResults
        fields = '__all__'