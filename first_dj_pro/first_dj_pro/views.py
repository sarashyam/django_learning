from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("Hi I'm Saradha.. This is my first django project")

def course(request):
    return HttpResponse("This is the course page")

def courseDetails(request,courseid):
    return HttpResponse(courseid)