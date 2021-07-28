from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    context_dict= {'boldmessage':'Rango says hey there partner!'}
    return render(request,'rango/index.html',context=context_dict)

def about(request):
    context_dict= {'boldmessage':'Rango sayshere is the about pages.'}
    return render(request,'rango/about.html',context=context_dict)