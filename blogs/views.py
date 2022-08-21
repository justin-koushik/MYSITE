from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import blog
from django.contrib import messages
from .forms import blogCreationForm,blogeditform
from urllib.parse import urlsplit
# Create your views here.
@login_required(login_url='login')
def blogs(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data=blog.objects.all()

    return render(request,'blogs/home.html',{'blogs':data,'homeActive':'active'})

def newblog(request):
    if request.method=='POST':
        form=blogCreationForm(request.POST)
        instance=form.save(False)
        instance.author=request.user
        instance.save()
        messages.success(request,'new blog created')
        return redirect('blog',permanent=True)
    form=blogCreationForm()
    return render(request,'blogs/blogcreate.html',{'form':form,'editActive':'active'})
def delete(request,blogid):
    item=blog.objects.get(id=blogid)
    item.delete()
    return redirect('blog',permanent=True)
def edit(request,blogid):
    item=blog.objects.get(id=blogid)
    if request.method=="POST":
        form=blogeditform(request.POST,instance=item)
        form.save()
        messages.success(request,'updated blog')
        next=request.POST.get('next')
        return redirect(next)
    form=blogeditform(instance=item)
    prevpath=request.META.get('HTTP_REFERER')
    splitted=urlsplit(prevpath)
    print(splitted)
    if splitted.path=="/":
        prevpath+=f"#{blogid}"
    return render(request,'blogs/editblog.html',{'form':form,'prevpath':prevpath,'path':request.get_host})
def save(request,blogid):
    text='unsave'
    item=blog.objects.get(id=blogid)
    if item in request.user.saved.all(): 
        request.user.saved.remove(item)
        text='save'
    else:
        request.user.saved.add(blog.objects.get(id=blogid))
    return JsonResponse({'text':text},safe=False)
def like(request,blogid):
    item=blog.objects.get(id=blogid)
    if request.user in item.likes.all():
        item.likes.remove(request.user)
    else:
        item.likes.add(request.user)
    return JsonResponse({'success':True})

def read(request,blogid):
    item=blog.objects.get(id=blogid)
    return render(request,'blogs/blog.html',{'blog':item})