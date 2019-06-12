from rest_framework.routers import DefaultRouter

from players.views import PlayersViewSet, PlayerStatsViewSet, ParticipationViewSet, TransfersViewSet

router = DefaultRouter()
router.register('', PlayersViewSet, base_name='players')
router.register('', PlayerStatsViewSet, base_name='playerStats')
router.register('', ParticipationViewSet, base_name='participation')
router.register('', TransfersViewSet, base_name='transfers')

urlpatterns = router.urls
