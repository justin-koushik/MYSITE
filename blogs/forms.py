from django import forms
from .models import blog
from django.utils import timezone
class blogCreationForm(forms.ModelForm):
    class Meta:
        model=blog
        fields=['title','intro','description']
    def save(self,commit=True):
        instance=super(blogCreationForm,self).save(commit=False)
        if commit:
            instance.save()
        return instance
class blogeditform(forms.ModelForm):
    class Meta:
        model=blog
        fields=['title','intro','description']
    def save(self):
        instance=super(blogeditform,self).save(commit=False)
        instance.posted=timezone.now()
        instance.save()