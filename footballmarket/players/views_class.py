from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from players.models import Club, Player


# PLAYERS CLASS

class PlayersListView(ListView):
    template_name = "players/list.html"
    model = Player



class PlayerCreateView(CreateView):
    model = Player
    fields = "__all__"
    template_name = "players/form.html"
    success_url = reverse_lazy("players:players-list-view")


class PlayerDetailView(DetailView):
    model = Player
    template_name = "players/player_detail.html"


# CLUBS CLASS

class ClubsListView(ListView):
    template_name = "players/list.html"
    model = Club
