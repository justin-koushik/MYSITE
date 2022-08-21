from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self,username,email=None,password=None,**other):
        if password is None:
            raise ValueError("password should be given")
        if email is None:
            raise ValueError("email should be given")
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,**other)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,email=None,password=None,**other):
        other.setdefault("is_staff",True)
        other.setdefault("is_superuser",True)
        other.setdefault("is_admin",True)
        other.setdefault("is_active",True)
        if not other.get('is_staff'):
            raise ValueError("is_staff is set false")
        if not other.get('is_superuser'):
            raise ValueError("is_superuser is set false")
        return self.create_user(username,email,password,**other)
    def get(self,*args,**kwargs):
        return super(UserManager,self).get(*args,**kwargs)

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(verbose_name=_("username"),max_length=20)
    fname=models.CharField(verbose_name=_("firstname"),max_length=20,blank=True)
    lname=models.CharField(verbose_name=_("lastname"),max_length=20)
    bdate=models.DateField(verbose_name=_("birth date"))
    email=models.EmailField(verbose_name="email",unique=True)
    about=models.TextField(verbose_name=_("tell about youself"),max_length=50,blank=True)
    date_joined=models.DateField(verbose_name=_('date joined'),auto_now_add=True)
    last_joined=models.DateField(verbose_name=_("last joined"),auto_now=True)
    saved=models.ManyToManyField('blogs.blog',verbose_name=_('saved blogs'),related_name='savedblogs')
    # profilepic=models.CharField(max_length=20,default="default")

    is_active=models.BooleanField(verbose_name=_("is active"),default=True)
    is_superuser=models.BooleanField(verbose_name=_("is superuser"),default=False)
    is_staff=models.BooleanField(verbose_name=_("is staff"),default=False)
    is_admin=models.BooleanField(verbose_name=_("is admin"),default=False)
    OBJECTS=UserManager()
    REQUIRED_FIELDS=['username','lname','fname','bdate']
    USERNAME_FIELD='email'
    def save(self,*args,**kwargs):
        if not self.id:
            self.date_joined=timezone.now()
        self.last_joined=timezone.now()
        return super(User,self).save(*args,**kwargs)