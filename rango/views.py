from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    html='<a href="/rango/about/">About</a>'
    return HttpResponse(html+"Rango says hey there partner!")


def about(request):
    html='<a href="/rango/">Index</a>'
    return HttpResponse("Rango says here is the about page."+html)