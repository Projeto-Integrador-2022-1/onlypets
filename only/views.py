from django.shortcuts import render
from clinicas import models

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
    clins=models.Clinica.objects.all()
    contexto={
        "clinicas": clins,
    }
    return render(request,"home/Clinica/clinicas.html",context=contexto)

def Vet(request):
    return render(request,"home/Vet/vets.html")


