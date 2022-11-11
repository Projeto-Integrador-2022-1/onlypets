from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from login.forms import Logando
from only.views import Homep

# Create your views here.

def HomeLogin(request):
    formulario = Logando()
    if request.method == 'POST':
        formulario=Logando(request.POST)
        if formulario.is_valid():
            usernames = formulario.cleaned_data['username']
            passwords = formulario.cleaned_data['password']
            user = authenticate(request, username=usernames,password=passwords)
            print(user)
            if user is not None:
                login(request,user)
                return redirect(Homep)
            else:
                formulario.add_error('password','Usuário ou senha incorretas')
    contexto={
    'form' : formulario, 
    }
    return render(request,"login/Login.html",context=contexto)

def Logout(request):
    logout(request)
    return redirect(HomeLogin)
