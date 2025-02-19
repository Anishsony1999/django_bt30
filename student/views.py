from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(req):
    return HttpResponse("Welcome Students")

def greeting(req,name):
    return HttpResponse("Welcome "+name)

def indexPage(req):
    return render(req,"index.html")