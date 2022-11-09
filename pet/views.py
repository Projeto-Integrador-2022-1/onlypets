from django.shortcuts import render

# Create your views here.

def PetCad(request):
    return render(request,"pet/PetCad.html")