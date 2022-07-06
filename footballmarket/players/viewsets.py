from players.models import Club

from rest_framework import viewsets

from players.serializers import ClubSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
