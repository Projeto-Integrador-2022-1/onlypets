from django import forms

class Logando(forms.Form):
    username = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'placeholder':'Usuário'}))

    password = forms.CharField(required=True,
            widget=forms.PasswordInput(attrs={'placeholder':'Senha'}))