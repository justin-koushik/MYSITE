from dataclasses import fields
from django.contrib import admin
from .models import blog
# from django.contrib.auth.admin import 
# # Register your models here.
# class blogAdmin(UserAdmin):
#     readonly_fields=['posted']
#     list_display=['title','author','posted']
#     fieldsets=(
#         ('title',{'fields':('title')}),
#     )
admin.site.register(blog)