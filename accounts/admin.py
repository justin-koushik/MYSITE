from typing import Any, Optional, Sequence
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import User

class userconAdmin(UserAdmin):
    readonly_fields=['date_joined','last_joined']
    search_fields=['username']
    list_filter=['is_active','is_admin']
    list_display=['username','email','fname','lname','bdate','is_superuser']
    fieldsets=((None,{"fields":('username','email')}),('personal',{'fields':('fname','lname','about','bdate','date_joined','last_joined','saved')}),('permission',{'fields':('is_active','is_staff','is_superuser','is_admin')}))
    add_fieldsets=(
        (None,{"classes":('wide'),'fields':('username','email','bdate','password1','password2')}),
    )
    ordering=['bdate']
    
admin.site.register(User,userconAdmin)