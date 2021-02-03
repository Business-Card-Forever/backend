from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView


from .serializers import UserSerializer,UserInfoSerializer,ConnectionSerializer,WorkExperienceSerializer,EductionSerializer

from .models import Connections, UserInfo,WorkExperience,Eduction

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserInfoViewSet(viewsets.ModelViewSet,RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes =[IsAuthenticated, ]
    
class ConnectionViewSet(viewsets.ModelViewSet,RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset =Connections.objects.all()
    serializer_class = ConnectionSerializer
    
class WorkExperienceViewSet(viewsets.ModelViewSet,RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset =WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer
    
class EductionViewSet(viewsets.ModelViewSet,RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset =Eduction.objects.all()
    serializer_class = EductionSerializer