from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class CompanyInfo(models.Model):
    company_name = models.CharField(max_length = 32 , blank =False , null = False,default='Null')
    company_id=models.OneToOneField(User,on_delete=models.CASCADE,default='Null')
    lanuch_date =models.DateField(blank=True, null=True,default='')   
    city = models.CharField(max_length = 32 , blank =False , null = False,default='Null')
    email =models.EmailField(max_length=254,default='user@gmail.com')
    aboutcompany = models.TextField(max_length = 255 , blank =False , null = False,default='Null')
    industry = models.CharField(max_length = 32 , blank =False , null = False,default='Null')
    num_emp = models.IntegerField()
    
    def __str__(self):
        return self.company_name
    
class CompanyEvents(models.Model):
    event_name = models.CharField(max_length = 64 , blank =False , null = False,default='Null')
    location = models.CharField(max_length = 64 , blank =False , null = False,default='Null')
    date = models.DateTimeField(blank=True, null=True,default='')
    desc = models.TextField(max_length = 255 , blank =False , null = False,default='Null')
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.event_name