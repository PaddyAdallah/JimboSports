from rest_framework import serializers

from .models import UserProfile, Team, Referee, Officials, Coach


# create serializers
class OfficialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officials
        fields = '__all__'
        # exclude = ('users',)
        # to exclude any unwanted fields


class RefereesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = '__all__'


class CoachesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


