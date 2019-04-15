from rest_framework import serializers
from .models import UserProfile, Team, Referee, Officials, Coach


# create serializers
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'phone', 'email', 'image', 'gender', 'user_type', 'user_id')


class TeamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'team_name', 'constituency', 'team_image')


