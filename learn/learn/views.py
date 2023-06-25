from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD   VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *


def index(request):
    return render(request,'index.html')
def first(request):
    return render(request,'index.html')


def userreg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myfile=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(myfile.name,myfile)
        registration=userdetails(name=name,phone=phone,email=email,password=password,image=myfile)
        registration.save()
    return render(request,'register.html',{'success':'Register  Successfully'})


def userv(request):
    user=userdetails.objects.all()
    return render(request,'userview.html',{'result':user})


def contactsave(request):
    a=request.session['uid']
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        file=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(file.name,file)
        registration=contactdetails(name=name,phone=phone,email=email,userid=a,image=file)
        registration.save()
    return render(request,'savecontact.html',{'success':'Saved  Successfully'})



def contactv(request):
    user=contactdetails.objects.all()
    return render(request,'viewcontact.html',{'result':user})


def userlogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email=='admin@gmail.com' and password == 'admin':
         request.session['logindetails'] = email
         request.session['admin'] ='admin'
         return render(request,'index.html')
        
    elif userdetails.objects.filter(email=email,password=password).exists():
        users=userdetails.objects.get(email=request.POST['email'],password=password)
        if users.password ==request.POST['password']:
                request.session ['uid']=users.id
                request.session ['uname']=users.email
                request.session ['email']=email
                request.session ['user']='user'
                return render(request,'index.html')
    else:
         return render(request,'login.html',{'success':'Login Successfully'})
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(index)

def profilev(request):
    tem=request.session['uid']
    vpro=userdetails.objects.get(id=tem)
    return render(request,'profileview.html',{'result':vpro})

def adminprofile(request):
    return render(request,'adminprofile.html')

def delete(request,id):
    member=contactdetails.objects.get(id=id)
    member.delete()
    return redirect(contactv)

def dele(request,id):
    member=userdetails.objects.get(id=id)
    member.delete()
    return redirect(userv)

def update(request,id):
    member=userdetails.objects.get(id=id)
    return render(request,'profileupdate.html',{'result':member})

def updates(request,id):
     if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myfile=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(myfile.name,myfile)
        registration=userdetails(name=name,phone=phone,email=email,password=password,image=myfile,id=id)
        registration.save()
        return redirect(profilev)


def uupdate(request,id):
    member=contactdetails.objects.get(id=id)
    return render(request,'contactupdate.html',{'result':member})


def uupdates(request,id):
    a=request.session['uid']
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        file=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(file.name,file)
        registration=contactdetails(name=name,phone=phone,email=email,userid=a,image=file,id=id)
        registration.save()
        return redirect(contactv)
    return render(request,'viewcontact.html')



