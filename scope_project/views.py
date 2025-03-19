from django.shortcuts import render

def handling_404(req,e):
    return render(req,'html_404.html',status=404)

def handling_500(req):
    return render(req,'html_404.html')