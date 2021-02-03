from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet , UserInfoViewSet,ConnectionViewSet,WorkExperienceViewSet,EductionViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)

router.register('userinfo',UserInfoViewSet)
router.register('connections',ConnectionViewSet)
router.register('workexperience',WorkExperienceViewSet)
router.register('eduction',EductionViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
