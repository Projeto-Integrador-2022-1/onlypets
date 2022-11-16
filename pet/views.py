from django.shortcuts import render, redirect
from pet.forms import Pet_Forms
# Create your views here.

def PetCad(request):
    formulario = Pet_Forms(initial={'user': request.user.id})
    
    if request.method == 'POST':
        formulario = Pet_Forms(request.POST)
        print("Cadastrado o pet1")
        if formulario.is_valid():
            if formulario.cleaned_data['pelagem'] == '-':
                formulario.add_error('pelagem','Por favor escolha um item')
            if formulario.cleaned_data['sexo'] == '-':
                formulario.add_error('sexo','Por favor escolha um item')
            print("Cadastrado o pet2")
            formulario.save()
        else:
            print('Erro')
            
    contexto={ 'form' : formulario,}
    return render(request,"pet/PetCad.html",context=contexto)