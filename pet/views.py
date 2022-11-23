from django.shortcuts import render, redirect
from pet.forms import Pet_Forms
from pet.models import Cadastro_Pet
# Create your views here.

def PetCad(request):
    formulario = Pet_Forms(initial={'user': request.user.id})
    
    if request.method == 'POST':
        formulario = Pet_Forms(request.POST,request.FILES)
        print("Cadastrado o pet1")
        if formulario.is_valid():
            print("Cadastrado o pet2")
            formulario.save()
        else:
            print('Erro')
    contexto={ 'form' : formulario,}
    return render(request,"pet/PetCad.html",context=contexto)

def ListaPet(request):
    pets = Cadastro_Pet.objects.filter(user=request.user.id)
    contexto={
        'pets' : pets
    }
    return render(request,"listapet/pets.html",context=contexto)