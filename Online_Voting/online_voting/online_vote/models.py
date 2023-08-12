from django.db import models
from django.db.models.fields.related import OneToOneField
from django.contrib.auth.models import User
class Userinfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Phone_Number=models.IntegerField(default=0)
    Address=models.TextField(max_length=200)
    Profile_Pic=models.ImageField()
    def __str__(self):
        return str(self.user)
class Candidate(models.Model):
    Name=models.CharField(max_length=50)
    Email_address=models.EmailField()
    Phone_No=models.IntegerField()
    Address=models.TextField(max_length=200)
    Electoral=models.ImageField()
    Votes=models.IntegerField(default=0)
    def __str__(self):
        return str(self.Name)
