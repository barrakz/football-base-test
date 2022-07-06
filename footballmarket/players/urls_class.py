from django.urls import path
from players import views_class


app_name = "players"

urlpatterns = [
    path("players-list-view/", views_class.PlayersListView.as_view(), name="players-list-view"),
    path("player-create-view/", views_class.PlayerCreateView.as_view(), name="player-create-view"),
    path("player-detail-view/<pk>", views_class.PlayerDetailView.as_view(), name="player-detail-view"),
    path("clubs-list-view/", views_class.ClubsListView.as_view(), name="clubs-list-view"),
]

