from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def datas(request):
    return HttpResponse("spectrum softech solution pvt ltd kochi")

def register(request):
    return render (request, 'register.html')

def login(request):
    return render (request, 'login.html')

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