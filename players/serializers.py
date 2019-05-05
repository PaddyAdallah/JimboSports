from rest_framework import serializers

from .models import Players, PlayersStats, Transfers, Participation


# create serializers
class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'
        # exclude = ('users',)
        # to exclude any unwanted fields


class PlayerStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayersStats
        fields = '__all__'


class TransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfers
        fields = '__all__'


class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = '__all__'
