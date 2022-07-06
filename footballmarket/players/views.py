from django.db.models import Avg
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from .models import Club, Player, Rating
from .serializers import ClubSerializer, PlayerSerializer, MatchesSerializer, RatingSerialize
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from .models import Match
from rest_framework.decorators import api_view
from rest_framework.views import APIView

def index(request):
    return HttpResponse("Hello on Player's site!")


class ClubsGeneric(ListCreateAPIView, generics.GenericAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class PlayerViewSet(generics.GenericAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


# @api_view(['GET', 'POST'])
# def matches_list(request):
#     matches = Match.objects.all()
#     serializer = MatchesSerializer(matches, many=True)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def match_create(request):
#     serializer = MatchesSerializer(data=request.data)
#     if serializer.is_valid():
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
#

class PlayersListCreate(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class RatingsCreate(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerialize

    def average_rating(self):
        return self.rate.aggregate(Avg('ratings'))['rating_avg']


