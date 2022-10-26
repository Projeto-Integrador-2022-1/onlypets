from cProfile import label
import email
from django import forms

class Cadastro_Form(forms.ModelForm):
    name = forms.CharField(label="Nome",widget=forms.TextInput())
    sobrenome = forms.CharField(label="Sobrenome",widget=forms.TextInput())
    email = forms.EmailField(label="Email",widget=forms.EmailInput())
    telefone = forms.CharField(label="Telefone",widget=forms.CharField())
    senha = forms.PasswordInput(label="Senha",widget=forms.PasswordInput())
    confirmar_senha = forms.CharFields(label="Senha",widget=forms.PasswordInput())
