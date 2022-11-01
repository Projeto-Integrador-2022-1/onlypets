from django.shortcuts import render
from django.contrib.auth.hashers import make_password
import cadastro
from cadastro.forms import Cadastro_Form, Login_Form
from cadastro.models import Cadastro_Pessoa

# Create your views here.

def Home(request):
    formulario = Cadastro_Form()
    contexto={
        'form' : formulario,
    }
    if request.method == 'POST':
        formulario = Cadastro_Form(request.POST)
        if formulario.is_valid():
           # if formulario.cleaned_data['Senha'] == formulario.cleaned_data['Confirmar_Senha']:
                novo = formulario.save()
                senha_cryp = make_password(request.POST['password'])
                novo.password = senha_cryp
                novo.save()
                perfil = Cadastro_Pessoa()
                perfil.Telefone = formulario.cleaned_data['telefone']
                perfil.user = novo
                perfil.save()

            #else:
                #formulario.add_error('As senhas não são iguais')

    return render(request,"cadastro/cadastro.html",context=contexto)

def login(request):
    form = Login_Form()
    contexto={
        'form' : form
        }
    return render(request,"cadastro/login.html",context=contexto)
