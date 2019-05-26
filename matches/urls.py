from rest_framework.routers import DefaultRouter

from matches.views import MatchFixturesViewSet, MatchResultsViewSet

router = DefaultRouter()
router.register('', MatchFixturesViewSet, base_name='matchFixtures')
router.register('', MatchResultsViewSet, base_name='matchResults')
urlpatterns = router.urls
