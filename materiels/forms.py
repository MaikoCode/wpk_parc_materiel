from django import forms
from .models import Materiel, Categorie, SousCategorie, Fournisseur
from .models import DemandeMateriel
from employe.models import Employe

class MaterielForm(forms.ModelForm):
    materiel_name = forms.CharField(label='Nom du matériel', max_length=100)
    num_serie = forms.CharField(label='Numéro de série', max_length=130)
    materiel_description = forms.CharField(label='Description', max_length=500)
    categorie = forms.CharField(label='Catégorie')
    sub_category = forms.CharField(label='Sous-catégorie')    
    new_category_name = forms.CharField(label='Nom de la catégorie', max_length=100, required=False)
    new_category_description = forms.CharField(label='Description de la catégorie', max_length=200, required=False)
    new_sub_category_name = forms.CharField(label='Nom de la sous-catégorie', max_length=100, required=False)
    new_sub_category_description = forms.CharField(label='Description de la sous-catégorie', max_length=200, required=False)

    class Meta:
        model = Materiel
        fields = ['materiel_name', 'num_serie', 'materiel_description', 'categorie', 'sub_category',
                  'new_category_name', 'new_category_description',
                  'new_sub_category_name', 'new_sub_category_description']

class MaterielUpdateForm(forms.ModelForm):
    materiel_name = forms.CharField(label='Nom du matériel', max_length=100)
    num_serie = forms.CharField(label='Numéro de série', max_length=130)
    materiel_description = forms.CharField(label='Description', max_length=500)

    class Meta:
        model = Materiel
        fields = ['materiel_name', 'num_serie', 'materiel_description']

class DemandeMaterielForm(forms.ModelForm):
    class Meta:
        model = DemandeMateriel
        fields = ['date_debut', 'description', 'materiel', 'demandeur']
        widgets = {
            'materiel': forms.HiddenInput(),
            'demandeur': forms.HiddenInput(),
        }
    date_debut = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'), label='Date de début d\'utilisation')
    description = forms.CharField(widget=forms.Textarea, label='Description de la demande', max_length=500)

class MaterielFilterForm(forms.Form):
    nomMateriel = forms.CharField(required=False)
    fournisseur = forms.ModelChoiceField(queryset=Fournisseur.objects.all(), required=False)
    sousCategorie = forms.ModelChoiceField(queryset=SousCategorie.objects.all(), required=False)
    isTaken = forms.BooleanField(required=False)
    enPanne = forms.BooleanField(required=False)