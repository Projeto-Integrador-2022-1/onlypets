from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Splash(request):
    return render(request,"home/Splash/Splash.html")

def Homep(request):
    return render(request,"home/Home/home.html")

def Login(request):
    return render(request,"home/Login_Cad/Login.html")

def Cadastro(request):
    return render(request,"home/Login_Cad/cadastro.html")

def Clinica(request):
    return render(request,"home/Clinica/clinicas.html")


