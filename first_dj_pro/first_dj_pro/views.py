from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {    
        'title':"HOME PAGE",
        'meow':"meow meow",
        'loop': ["hai","hello","meow"],
        'di_list':[
                {'name':"meow", 'num':"876555454"},
                {'name':"bow", 'num':"65156456554"}
            ]
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Hi I'm Saradha.. This is my first django project")

def course(request):
    return HttpResponse("This is the course page")

def courseDetails(request,courseid):
    return HttpResponse(courseid)