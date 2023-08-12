

from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import SignUp,UserInfo,candidate
from .models import Userinfo,Candidate
@login_required
def addvoter(request):
    if request.user.is_superuser:
        form=candidate    
        if request.method=="POST":
            form=candidate(data=request.POST,files=request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request,'online_vote/addvoter.html',{'form':form})
@login_required
def viewprof(request):
    prof=request.user


    userinfo=Userinfo.objects.get(user=request.user)
    
    username = request.user.username
    user=User.objects.get(username=username)
    superuser=(request.user.is_superuser)


    return render(request,"online_vote/profile.html",{'superuser':superuser,'Phone_Number':userinfo.Phone_Number,'Address':userinfo.Address,"Profile_Pic":userinfo.Profile_Pic,
    'email':user.email,
    "username":user.username

})
@login_required
def home(request):
    prof=request.user
    alluser=Candidate.objects.all()

    userinfo=Userinfo.objects.get(user=request.user)
    
    print(userinfo.Profile_Pic)
    username = request.user.username
    user=User.objects.get(username=username)
    superuser=(request.user.is_superuser)


    return render(request,"online_vote/home.html",{'superuser':superuser,'Phone_Number':userinfo.Phone_Number,'Address':userinfo.Address,"Profile_Pic":userinfo.Profile_Pic,
    'email':user.email,
    "username":user.username,"alluser":alluser,'vote':user.last_name

})
@login_required
def showresult(request):
    if request.user.is_superuser:
    
        alluser=Candidate.objects.all()
        temp=0
        winner="NoOne"
        for candidate in alluser:
            a=candidate.Votes
            if temp<a:
                temp=a
                winner=candidate.Name
        return render(request,"online_vote/result.html",{"alluser":alluser,'winner':winner,'totalvotes':temp  })
@login_required
def inc(request,pk):
    # if request.user.is_authenticated():
        username = request.user.username
        user=User.objects.get(username=username)
        if user.last_name!="True":
            candi=Candidate.objects.get(id=pk)      
            candi.Votes=candi.Votes+1
            candi.save()
            user.last_name="True"
            user.save()
            return redirect('/')
        
def Signup(request):
    form=SignUp()
    form1=UserInfo()
    if request.method=="POST":
        form=SignUp(data=request.POST)
        form1=UserInfo(data=request.POST,files=request.FILES)

        if True:
            user=form.save(commit=False)
            user.set_password(user.password)
            user.save()
            uf=form1.save(commit=False)
            uf.user=user
            uf.save()
            
            return HttpResponseRedirect("/accounts/login")
    return render(request,'online_vote/SignUp.html',{'form':form,'form1':form1})