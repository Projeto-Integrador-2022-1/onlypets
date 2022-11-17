from django.shortcuts import render, redirect
from pet.forms import Pet_Forms
# Create your views here.

def PetCad(request):
    formulario = Pet_Forms(initial={'user': request.user.id})
    
    if request.method == 'POST':
        formulario = Pet_Forms(request.POST)
        print("Cadastrado o pet1")
        if formulario.is_valid():
            print("Cadastrado o pet2")
            formulario.save()
        else:
            print('Erro')
    contexto={ 'form' : formulario,}
    return render(request,"pet/PetCad.html",context=contexto)