from datetime import date
from django import forms


class EmployeForm(forms.Form):
    # username = forms.CharField(max_length=63, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password = forms.CharField(max_length=63, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nom = forms.CharField(max_length=63, label='Nom', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Nom'}))
    prenom = forms.CharField(max_length=63, label='Prénom', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Prénom'}))
    poste = forms.CharField(max_length=63, label='Poste',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Poste'}))
    dateEmbauche = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))