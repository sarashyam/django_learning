from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("Hi I'm Saradha.. This is my first django project")

def course(request):
    return HttpResponse("This is the course page")

def courseDetails(request,courseid):
    return HttpResponse(courseid)