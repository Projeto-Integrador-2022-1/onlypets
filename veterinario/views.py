from django.shortcuts import render
from veterinario.forms import Cadastro_Servico

# Create your views here.

def Cad_Servico(request):
    formulario = Cadastro_Servico(initial={'user': request.user.id})
    
    if request.method == 'POST':
        formulario = Cad_Servico(request.POST)
        if formulario.is_valid():
            formulario.save()
    contexto={
        'form' : formulario
    }
    return render(request,"cadservico/cadservc.html",context=contexto)

