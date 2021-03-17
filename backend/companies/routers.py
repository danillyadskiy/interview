from rest_framework import routers

from companies.api import *

router = routers.SimpleRouter(trailing_slash=False)

router.register('region', RegionSet)
router.register('company', CompanySet, basename='Company')

urlpatterns = router.urls
