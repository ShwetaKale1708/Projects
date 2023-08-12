from os import getcwd,chdir
from django.http.response import HttpResponse
from django.shortcuts import render
from . import forms
from .main import pp
import requests
import  shutil
from random import  randint
from PIL import Image
from os.path import join
def home(request):
    # a='/media/842982I2S.jpg'
    # return render(request,'ImageApp/show.html',{'dir':a})
    try:    
        homeform=forms.form()
        choices=forms.option()
        if request.method=="POST":
            choices=forms.option(data=request.POST)
            homeform=forms.form(data=request.POST,files=request.FILES)
            imgf=0
            try:
                imgf=request.FILES['Image']
            except:
                pass
            # print("Url",request.POST['Url'],ipel)
            if imgf!=0:
                if homeform.is_valid(): 
                    k=request.FILES['Image']
                    homeform.save()
                    cho=request.POST['choicefield']
                    if '.jpg' or '.jpeg' or '.png':
                        k=str(k)  
                        dir=pp(k,cho)
                    
                        dir='/media/'+str(dir)
                        return render(request,'ImageApp/show.html',{'dir':dir})
            elif str(request.POST['Url']):
                    url=str(request.POST['Url'])
                
                    
                    name=str(randint(111111,999999))+".jpg"
                    orgdir=getcwd()
                    chgedir=getcwd()+'/media'
                    print("EL")
                    chdir(chgedir)
                    print(url,name)
                    import requests
                    response = requests.get(url)

                    file = open(name, "wb")
                    file.write(response.content)
                    file.close()
                    chdir(orgdir)
                    cho=request.POST['choicefield']
                        
                    dir=pp(name,cho)
                    
                    dir='/media/'+str(dir)
                    print(dir)
                    return render(request,'ImageApp/show.html',{'dir':dir})

    except:
        pass
        
                
    return render(request,'ImageApp/home.html',{'homeform':homeform,'optionform':choices})