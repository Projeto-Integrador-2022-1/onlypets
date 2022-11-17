from django import forms
from django.contrib.auth.models import User
from clinicas.models import Clinica
from veterinario.models import Servico

class Cadastro_Vet_Form(forms.ModelForm):
    telefone = forms.CharField(max_length=11,widget=forms.TextInput(attrs={'placeholder':'Telefone'}))
    crmv = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'CRMV'}))
    clinica = forms.ModelChoiceField(queryset=Clinica.objects.all())

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

class Cadastro_Servico(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'placeholder':'Serviço'}),
            'preco' : forms.NumberInput(attrs={'placeholder': 'Preço'}),
            'seg' : forms.CheckboxInput(attrs={'class':'dia'}),
            'ter' : forms.CheckboxInput(attrs={'class':'dia'}),
            'qua' : forms.CheckboxInput(attrs={'class':'dia'}),
            'qui' : forms.CheckboxInput(attrs={'class':'dia'}),
            'sex' : forms.CheckboxInput(attrs={'class':'dia'}),
            'sab' : forms.CheckboxInput(attrs={'class':'dia'}),
        }