from django.shortcuts import render
from veterinario.forms import Cadastro_Servico

# Create your views here.

def Cad_Servico(request):
    formulario = Cadastro_Servico()
    contexto={
        'form' : formulario
    }
    return render(request,"cadservico/cadservc.html",context=contexto)

