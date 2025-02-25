from django.shortcuts import render,redirect
from django.http import HttpResponse

students = [
    "Anish",
    "Abi",
    "sonu"
] # student/find/2 - User Not Fount

def index(request):
    return HttpResponse("Welcome Students")

def greeting(request,name):
    return HttpResponse("Welcome "+name)

def indexPage(request):

    page_name = 'Sony Site'
    title = 'Index'
    return render(request,"index.html",{"title":title,'name':page_name})

def about(request):
    return render(request,'about.html')

def find(request,num):
    if 0 < num < 4 :
        user_name = students[num - 1]
        return render(request,"index.html",{'name':user_name})
    else:
        user_name = "User NOT Fount"
        return render(request,"index.html",{'name':user_name})

def show_contact(request):
    return render(request,'contact.html')

def index2(request):
    return render(request,"index2.html")

def home(req):
    return render(req,"home.html")

def projects(req):
    return HttpResponse("Projects")

def show_products(req):


    return render(req,"products.html",{"products":students})
