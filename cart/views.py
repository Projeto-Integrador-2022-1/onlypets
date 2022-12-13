from django.shortcuts import render
from veterinario.models import Servico

def Carrinho(request,id):
    
    servicos =Servico.objects.filter(user=id)
    contexto={
        "servicos" : servicos
    }
    return render(request,"Carrinho/carrinhovrs2.html",context=contexto)
