from cProfile import label
import email
from django import forms
from matplotlib import widgets

from cadastro.models import Cadastro_Pessoa

class Cadastro_Form(forms.ModelForm):
    class Meta:
        model = Cadastro_Pessoa
        fields  = '__all__'
        widgets = {

            'Nome' : forms.TextInput(attrs={'placeholder':'Nome'}),
            'Sobrenome' : forms.TextInput(attrs={'placeholder':'Sobrenome'}),
            'Email' : forms.EmailInput(attrs={'placeholder':'Email'}),
            'Telefone' : forms.TextInput(attrs={'placeholder':'Telefone'}),
            'Senha': forms.PasswordInput(attrs={'placeholder':'Senha'}),
            'Confirmar_Senha': forms.PasswordInput(attrs={'placeholder':'Confirmar Senha'})
        }
   
