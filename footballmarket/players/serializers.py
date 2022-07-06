from rest_framework import serializers
from players.models import Club, Player, Match, Rating


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ('club_name',)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'age', 'club',)


class MatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'


class RatingSerialize(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
