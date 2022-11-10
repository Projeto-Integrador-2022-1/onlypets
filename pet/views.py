from django.shortcuts import render
from pet.forms import Pet_Forms

# Create your views here.

def PetCad(request):
    formulario = Pet_Forms(initial={'user': request.user.id})
    contexto={
        'form' : formulario,
    }
    if request.method == 'POST':
        formulario = Pet_Forms(request.POST)
        print("Cadastrado o pet1")
        if formulario.is_valid():
            formulario.save()
            print("Cadastrado o pet2")
        else:
            print('Erro')
    return render(request,"pet/PetCad.html",context=contexto)