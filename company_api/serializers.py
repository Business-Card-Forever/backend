from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import CompanyInfo,CompanyEvents

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs={'password':{'write_only':True, 'required':True}}
    
    def create(self,validate_data):
        user = User.objects.create_user(**validate_data)
        Token.objects.create(user=user)
        return user
    
class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = ['id','company_name','company_id','lanuch_date','city','email','aboutcompany','industry','num_emp']

class CompanyEventsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'event_name', 'location', 'date','desc','host')
        model = CompanyEvents