from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Splash(request):
    return render(request,"polls/Splash.html")
