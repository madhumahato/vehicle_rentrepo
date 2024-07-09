from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(requset): 
    if requset.method=='POST':
        name=requset.POST['name']
        email=requset.POST['email']
        phone=requset.POST['phone']
        message=requset.POST['message']
        if User.objects.filter(username=name).exists():
            messages.info(requset,"username is already exist")
            return redirect('index')
        elif User.objects.filter(email=email).exists():
            messages.success(requset,"email is already exist in datebase")
        elif User.objects.filter(phone=phone).exists():
            messages.success(requset,"phone number is already exist in datebase")    
        else:
            user=User.objects.create_user(username=name,email=email,phone=phone)
            user.save()
            messages.success(requset,"sucessfully register !!!!!!")
            return redirect('index')           
    current_date = datetime.now().year
    return render(requset, "index.html", {'date':current_date})
def contact_form(requset):
    current_date = datetime.now().year
    return render(requset, "contact.html", {'current':current_date})
def signup_up_form(requset):
    if requset.method=='POST':
        username=requset.POST['username']
        email=requset.POST['email']
        password=requset.POST['password']
        password1=requset.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(requset,"username is already exist")
                return redirect('singup_form')
            elif User.objects.filter(email=email).exists():
                messages.success(requset,"email is already exist in datebase")
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(requset,"sucessfully register !!!!!!")
                return redirect('login_form')
        else:
            messages.info(requset,"password doesnot match!!")  
            return redirect('singup_form')  
    return render(requset, "signup.html")
def login_form(requset):
    if requset.method=='POST':
        username=requset.POST['username']
        password=requset.POST['password']
        if not User.objects.filter(username=username).exists():
                messages.error(requset,"invalid username")
                return redirect('login_form')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(requset,user)
            return redirect('index')
        else:
            messages.error(requset,'invalid password')
            return redirect('login_form')
    return render(requset, "login.html")
def logout_form(requset):
    if requset.method=='POST':
        username=requset.POST['username']
        password=requset.POST['password']
        if not User.objects.filter(username=username).exists():
                messages.error(requset,"invalid username")
                return redirect('logout_form')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(requset,user)
            return redirect('index')
        else:
            messages.error(requset,'invalid password')
            return redirect('logout_form')
    return render(requset, "logout.html")