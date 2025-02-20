from django.shortcuts import render,redirect
from django.http import HttpResponse

Students = [
    "Anish",
    "Abi",
    "sonu"
] # student/find/2 - User Not Fount

def index(req):
    return HttpResponse("Welcome Students")

def greeting(req,name):
    return HttpResponse("Welcome "+name)

def indexPage(req):
    page_name = 'Sony Site'
    title = 'Index'
    return render(req,"index.html",{"title":title,'name':page_name})

def about(req):
    return render(req,'about.html')