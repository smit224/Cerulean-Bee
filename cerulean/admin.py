from django.contrib import admin
from .models import *

# Register your models here.

class UserListShow(admin.ModelAdmin):
    list_display = ['user_id','username', 'email_id','password']

admin.site.register(SystemUser,UserListShow)
admin.site.register(ArtworkOrder)