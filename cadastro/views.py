from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from cadastro.forms import Cadastro_Form
from cadastro.models import Cadastro_Pessoa

# Create your views here.

def HomeCad(request):
    formulario = Cadastro_Form()
    contexto={
        'form' : formulario,
    }
    if request.method == 'POST':
        formulario = Cadastro_Form(request.POST)
        if formulario.is_valid():
                novo = formulario.save()
                senha_cryp = make_password(request.POST['password'])
                novo.password = senha_cryp
                novo.save() 
                perfil = Cadastro_Pessoa()
                perfil.Telefone = formulario.cleaned_data['telefone']
                perfil.user = novo
                perfil.save()
                
    return render(request,"cadastro/cadastro.html",context=contexto)