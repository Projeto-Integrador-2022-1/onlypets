from django.shortcuts import render
from cadastro.forms import Cadastro_Form

# Create your views here.

def Home(request):
    formulario = Cadastro_Form
    contexto={
        'form' : formulario,
    }
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
    return render(request,"cadastro/cadastro.html",context=contexto)