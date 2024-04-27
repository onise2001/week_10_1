from django.http import HttpResponse


def homepage(request):
    return HttpResponse("<h1>This is the HOME page.</h1>")

def aboutpage(request):
    return HttpResponse("<h1>This is the ABOUT page.</h1>")

def contactpage(request):
    return HttpResponse("<h1>This is the CONTACT page.</h1>")

def index(request):
    return HttpResponse("<h1>This is the INDEX page.</h1>")