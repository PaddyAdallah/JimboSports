from rest_framework import serializers

from .models import League, LeagueTeam


# create serializers
class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'
        # exclude = ('users',)
        # to exclude any unwanted fields


class LeagueTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueTeam
        fields = '__all__'
