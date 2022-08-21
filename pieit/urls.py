"""pieit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts import views as account
from django.contrib.auth.views import PasswordChangeView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("blogs.urls")),
    path('myaccount/changePassword',PasswordChangeView.as_view(template_name='accounts/password.html', success_url='/myaccount/',),name='changePassword'),
    path("register/",account.register,name='register'),
    path('myaccount/',account.myaccount,name='myself'),
    path('myaccount/edit',account.editProfile,name='edit'),
    path("login/",account.Login,name='login'),
    path('logout/',account.Logout,name='logout'),
    path('myaccount/reset',PasswordResetView.as_view(template_name='accounts/reset.html'),name='reset'),
    path('myaccount/reset/done',PasswordResetDoneView.as_view(template_name='accounts/reset_done.html'),name='password_reset_done'),
    path('myaccount/reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='accounts/reset-confirm.html'),name='password_reset_confirm'),
]
