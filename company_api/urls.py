from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from .views import UserViewSet,CompanyInfoSerializerViewSet,CompanyEventsSerializerViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)

router.register('companyinfo',CompanyInfoSerializerViewSet)
router.register('companyevents',CompanyEventsSerializerViewSet)



urlpatterns = [
    path('',include(router.urls)),
]
