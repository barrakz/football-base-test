from players.viewsets import ClubViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clubs', ClubViewSet)

