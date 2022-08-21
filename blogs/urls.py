from django.urls import path
from .views import blogs,newblog,delete,edit,save,like,read
urlpatterns = [
    path("",blogs,name="blog"),
    path('newblog/',newblog,name='newblog'),
    path('delete/<int:blogid>',delete,name='delete'),
    path('edit/<int:blogid>',edit,name='edit'),
    path('save/<int:blogid>',save,name='save'),
    path('like/<int:blogid>',like,name='like'),
    path('read/<int:blogid>',read,name='read')
]