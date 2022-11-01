from django.shortcuts import render

# Create your views here.

def HomeLogin(request):
    return render(request,"login/Login.html")