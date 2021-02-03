from django.contrib import admin

from .models import UserInfo,Connections,WorkExperience,Eduction
# Register your models here.

admin.site.register(UserInfo)
admin.site.register(Connections)
admin.site.register(WorkExperience)
admin.site.register(Eduction)