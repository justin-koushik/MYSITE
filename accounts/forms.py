from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model
from django import forms
user=get_user_model()
class registerForm(UserCreationForm):
    class Meta:
        model=user
        fields=['fname','lname','username','email','bdate','about']
        widgets = {
            'bdate': forms.DateInput(attrs={'type': 'date'})
        }


class Loginform(forms.Form):
    username = UsernameField(widget=forms.EmailInput(
        attrs={
        'class':'form-control',
        'placeholder':'....@example.com',
        'name':'username',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
        'class':'form-control',
        'placeholder':'********'
        }
    ))

class editForm(forms.ModelForm):
    class Meta:
        model=user
        fields=['username','fname','lname','email','bdate','about']
