from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.postgres.fields import ArrayField



from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    full_name = models.CharField(max_length = 32 , blank =False , null = False,default='Null')
    userinfo=models.OneToOneField(User,on_delete=models.CASCADE,default='Null')
    birthday =models.DateField(blank=True, null=True,default='')   
    city = models.CharField(max_length = 32 , blank =False , null = False,default='Null')
    email =models.EmailField(max_length=254,default='user@gmail.com')
    aboutme = models.TextField(max_length = 255 , blank =False , null = False,default='Null')
    major = models.CharField(max_length = 32 , blank =False , null = False,default='Null')
    # phone = PhoneNumberField(null=False, blank=False, unique=True,default='Null')
    # workexperience= ArrayField(models.CharField(max_length=200, blank =False , null = False),default=list)
    # eductions = ArrayField(models.CharField(max_length=15),default=list)

    
    
    def __str__(self):
        return self.full_name
    
    
class Connections(models.Model):
    userid = models.ManyToManyField(User,related_name='userid_set')
    connectionid = models.ManyToManyField(User)
    
    def __str__(self):

        return str(User.userid_set)


class WorkExperience(models.Model):
    org_name = models.CharField(max_length = 64 , blank =False , null = False,default='Null')
    position = models.CharField(max_length = 64 , blank =False , null = False,default='Null')
    date = models.DateField(blank=True, null=True,default='')
    desc = models.TextField(max_length = 255 , blank =False , null = False,default='Null')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):

        return self.org_name
    
    
class Eduction(models.Model):
    institute_name = models.CharField(max_length = 64 , blank =False , null = False,default='Null')
    degree = models.CharField(max_length = 64 , blank =False , null = False,default='Null')
    date = models.DateField(blank=True, null=True,default='')
    desc = models.TextField(max_length = 255 , blank =False , null = False,default='Null')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):

        return self.institute_name
