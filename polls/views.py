from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Splash(request):
    return render(request,"polls/Splash/Splash.html")

def Homep(request):
    return render(request,"polls/Home/home.html")

def Login(request):
    return render(request,"polls/Login_Cad/Login.html")

def Cadastro(request):
    return render(request,"polls/Login_Cad/cadastro.html")
