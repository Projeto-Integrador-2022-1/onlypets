from django import forms
from pet.models import Cadastro_Pet

class Pet_Forms(forms.ModelForm):
    class Meta:
        model = Cadastro_Pet
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'placeholder':'Nome do Pet'}),
            'peso' : forms.TextInput(attrs={'placeholder':'Peso do Pet (opcional)', 'required':False}),
            'nascimento' : forms.TextInput(attrs={'placeholder':'Data de nascimento (opcional)', 'required':False}),
            'especie' : forms.TextInput(attrs={'placeholder':'Espécie'}),
            'sexo' : forms.Select(),
            'raca' : forms.TextInput(attrs={'placeholder':'Raça do Pet'}),
            'pelagem' : forms.Select(),
            'imagemPet' : forms.FileInput(attrs={'required':False}),
            'user' : forms.HiddenInput(),
        }
