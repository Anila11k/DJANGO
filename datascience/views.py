from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



def datas(request):
    return HttpResponse("spectrum softech solution pvt ltd kochi")

def register(request):
    if request.method=='POST':
        username= request.POST.get('username','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        confirm_password=request.POST.get('confirm_password','')


        if not username or not email or not password:
            messages.error(request,'All field are required!.')
        elif password !=confirm_password:
            messages.error(request,'password do not match')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username already exists ')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already exists ')  
        else:

            user=User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request,'Account created successfully ! please login')
        return redirect('login_view')
    return render(request,'register.html')              


        
    

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username','')
        password=request.POST.get('password','')


        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request,'login.html')

def homepage(request):
    return render (request,'homepage.html')

def recommand(request):
    return render (request,'recommand.html')

def about(request):
    return render (request,'about.html')

def contact(request):
    return render (request,'contact.html')


def movies(request):
    return render (request,'movies.html')

def index(request):
    return render(request,'index.html')











