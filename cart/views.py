from django.shortcuts import render
from veterinario.models import Servico
from pet.models import Cadastro_Pet

def Carrinho(request,id):
    pets = Cadastro_Pet.objects.filter(user=request.user.id)
    servicos =Servico.objects.filter(user=id)
    contexto={
        'pets' : pets,
        "servicos" : servicos
    }
    return render(request,"Carrinho/carrinhovrs2.html",context=contexto)

def conf_pag(request,id):
    return render(request,"Conf_pagamento/conf.html")

def histo(request,id):
    return render(request,"histo/hist.html")