from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import is_valid_path
from login.forms import Logando

# Create your views here.

def HomeLogin(request):
    formulario = Logando()
    contexto={
        'form' : formulario, 
    }
    if request.method == 'POST':
        print("Frase qualquer")
        formulario= Logando(request.POST)
        if formulario.is_valid():
            print("Outra frase")
            usernames = formulario.cleaned_data['username']
            passwords = formulario.cleaned_data['password']
            user = authenticate(request, username=usernames,password=passwords)
            print(user)
            if user is not None:
                login(request,user)
            else:
                formulario.add_error("Algo de errado não está certo")
    return render(request,"login/Login.html",context=contexto)