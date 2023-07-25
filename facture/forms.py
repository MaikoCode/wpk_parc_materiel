from django import forms
from .models import Facture, LigneFacture, Fournisseur, Article

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['fournisseur', 'date_facture', 'numero_facture']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        # Créer un champ de sélection pour le fournisseur en utilisant une liste de choix
        #self.fields['fournisseur'].widget = forms.Select(choices=Fournisseur.objects.all().values_list('id', 'nom'))
        self.fields['fournisseur'].queryset = Fournisseur.objects.all()

class LigneFactureForm(forms.ModelForm):
    class Meta:
        model = LigneFacture
        fields = ['article', 'quantite']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        # Créer un champ de sélection pour la marchandise en utilisant une liste de choix
        # self.fields['marchandise'].widget = forms.Select(choices=Marchandise.objects.all().values_list('id', 'nom'))