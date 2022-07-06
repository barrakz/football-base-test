from django.urls import path
from players import views
from players.views import ClubsGeneric, PlayersListCreate, RatingsCreate
# from players.views import matches_list, match_create


urlpatterns = [
    path('playerspage/', views.index, name='index'),
    path('generic-clubs/', ClubsGeneric.as_view()),
    # path('matches-list/', matches_list),
    # path('create-match/', match_create),
    path('players-list-create/', PlayersListCreate.as_view(), name="players-list-create"),
    path('ratings/', RatingsCreate.as_view(), name="ratings"),
    # path('average-rating/', AverageRating.as_view(), name="average-rating"),

]

