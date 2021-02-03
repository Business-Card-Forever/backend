from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import UserInfo,Connections,WorkExperience,Eduction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs={'password':{'write_only':True, 'required':True}}
    
    def create(self,validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id','full_name','userinfo','birthday','city','email','aboutme','major']
        
class ConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connections
        fields = ['id','userid','connectionid']
        
        
class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'org_name', 'position', 'date','desc','user')
        model = WorkExperience
        
class EductionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'institute_name', 'degree', 'date','desc','user')
        model = Eduction
