from rest_framework.routers import DefaultRouter

from users.views import OfficialsViewSet, RefereesViewSet, CoachesViewSet, UserProfileViewSet, TeamsViewSet

router = DefaultRouter()
router.register('', OfficialsViewSet, base_name='officials')
router.register('', RefereesViewSet, base_name='referees')
router.register('', CoachesViewSet, base_name='coaches')
router.register('', UserProfileViewSet, base_name='userProfiles')
router.register('', TeamsViewSet, base_name='teams')

urlpatterns = router.urls
