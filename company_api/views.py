from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView


from .serializers import CompanyInfoSerializer,CompanyEventsSerializer,UserSerializer
from .models import CompanyEvents,CompanyInfo


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompanyInfoSerializerViewSet(viewsets.ModelViewSet,RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes =[IsAuthenticated, ]

class CompanyEventsSerializerViewSet(viewsets.ModelViewSet,RetrieveUpdateDestroyAPIView,CreateAPIView):
    queryset = CompanyEvents.objects.all()
    serializer_class = CompanyEventsSerializer

