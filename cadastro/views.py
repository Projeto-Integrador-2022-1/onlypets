from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from cadastro.forms import Cadastro_Form
from cadastro.models import Cadastro_Pessoa
from veterinario.forms import Cadastro_Vet_Form

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

def VetCad(request):
    formulario = Cadastro_Vet_Form()
    contexto={
        'form' : formulario,
    }
    if request.method == 'POST':
        formulario = Cadastro_Vet_Form(request.POST)
        if formulario.is_valid():
            novo = formulario.save()
            senha_cryp = make_password(request.POST['password'])
            novo.password = senha_cryp
            novo.save() 
            perfil = Cadastro_Pessoa()
            perfil.Telefone = formulario.cleaned_data['telefone']
            perfil.Crmv = formulario.cleaned_data['crmv']
            perfil.Clinica = formulario.cleaned_data['clinica']
            perfil.user = novo
            perfil.save()
            
    return render(request,"veterinario/vetcad.html",context=contexto)