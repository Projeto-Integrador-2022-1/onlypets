from django import forms
from django.contrib.auth.models import User

class Cadastro_Form(forms.ModelForm):
    telefone = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'placeholder':'Telefone'}))
    class Meta:
        model = User
        fields  = ['username','first_name','last_name','email','password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder':'Nome do usuário'}),
            'first_name' : forms.TextInput(attrs={'placeholder':'Nome'}),
            'last_name' : forms.TextInput(attrs={'placeholder':'Sobrenome'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Senha'}),
        }
   
