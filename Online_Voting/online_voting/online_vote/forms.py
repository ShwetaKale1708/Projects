from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Userinfo,Candidate
 
class SignUp(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','password','email']
class UserInfo(forms.ModelForm):
    class Meta:
        model=Userinfo
        fields=['Phone_Number','Address','Profile_Pic']

class candidate(forms.ModelForm):
    class Meta:
        model=Candidate
        fields=['Name','Email_address','Phone_No','Address','Electoral']