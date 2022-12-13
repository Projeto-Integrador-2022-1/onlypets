from django.shortcuts import render
from veterinario.models import Servico
from cadastro.models import Cadastro_Pessoa

def Carrinho(request,id):
    
    servicos =Servico.objects.filter(user=id)
    return render(request,"Carrinho/carrinhovrs2.html")
