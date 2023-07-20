from django.db import models
from fournisseur.models import Fournisseur
class Categorie(models.Model):
    idCategory = models.AutoField(primary_key=True)
    nomCategory = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class SousCategorie(models.Model):
    idSousCategorie = models.AutoField(primary_key=True)
    nomSousCategory = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

class Materiel(models.Model):
    idMateriel = models.AutoField(primary_key=True)
    nomMateriel = models.CharField(max_length=100)
    NumSerie = models.CharField(max_length=130)
    description = models.CharField(max_length=500)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_DEFAULT, default=1)
    sous_categorie = models.ForeignKey(SousCategorie, on_delete=models.SET_DEFAULT, default=1)
    is_taken = models.BooleanField(default=False)
    en_panne = models.BooleanField(default=False)