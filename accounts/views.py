from django.shortcuts import render
from .forms import registerForm,editForm,Loginform
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from blogs.models import blog
from .models import User
from multiavatar.multiavatar import multiavatar
import random as r

def register(request):
    if(request.method=='POST'):
        form=registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            return render(request,'accounts/register.html',{'form':form})
    form=registerForm()
    return render(request,'accounts/register.html',{'form':form})
    
def Login(request):
    if request.user.is_authenticated:
        return redirect('blog')
    if request.method=="POST":
        form=Loginform(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:    
            login(request,user)
            return redirect('blog')
        else:
            messages.warning(request,'username or password may invalid')
            return render(request, 'accounts/login.html', {'form':form})
    else:
        form=Loginform()
        return render(request,'accounts/login.html',{'form':form})
@never_cache
def Logout(request):
    logout(request)
    messages.success(request,'successfully logged out!')
    return redirect('login')
@login_required(login_url='login')
def myaccount(request):
    if not request.user.is_authenticated:
        return redirect('login')
    posts=blog.objects.filter(author=request.user)
    id=str(request.user.id)
    pic=multiavatar(id,True,None)
    savedblogs=request.user.saved.all()
    likedblogs=request.user.likes.all()
    return render(request,'blogs/account.html',{'posts':posts,'profilepic':pic,'savedblogs':savedblogs,'accActive':'active','likedblogs':likedblogs})
@login_required(login_url='login')   
def editProfile(request):
    if request.method=='POST':
        form=editForm(request.POST,instance=request.user)
        messages.success(request,'profile changed successfully')
        form.save()
        return redirect('myself')
    form=editForm(instance=request.user)
    return render(request,'accounts/edit.html',{'form':form})

