from django.shortcuts import render
from cadastro.forms import Cadastro_Form

# Create your views here.

def Home(request):
    formulario = Cadastro_Form()
    contexto={
        'form' : formulario,
    }
    if request.method == 'POST':
        formulario = Cadastro_Form(request.POST)
        if formulario.is_valid():
            if formulario.cleaned_data['Senha'] == formulario.cleaned_data['Confirmar_Senha']:
                formulario.save()
            else:
                formulario.add_error('As senhas não são iguais')

    return render(request,"cadastro/cadastro.html",context=contexto)