from statistics import mode
from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from django.utils import timezone
from django_quill.fields import QuillField
user=get_user_model()

class blog(models.Model):
    title=models.CharField(verbose_name="title",max_length=50)
    posted=models.DateField(verbose_name="posted on",default=timezone.now(),editable=False)
    intro=models.TextField(verbose_name='introduction',null=False)
    description=QuillField()
    author=models.ForeignKey(user,on_delete=models.CASCADE,related_name='written')
    likes=models.ManyToManyField(user,related_name='likes')
    def __str__(self):
        return f'{self.title}-{self.posted}'