from django import forms
from .models import Fournisseur

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nomFournisseur', 'adresse', 'email', 'telephone']
