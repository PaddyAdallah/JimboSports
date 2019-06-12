from rest_framework.routers import DefaultRouter

from league.views import LeagueViewSet, LeagueTeamsViewSet

router = DefaultRouter()
router.register('', LeagueViewSet, base_name='leagues')
router.register('', LeagueTeamsViewSet, base_name='leagueTeams')
urlpatterns = router.urls
