from django.db import models
from employe.models import Employe
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

    def __str__(self):
        return self.nomSousCategory
class Materiel(models.Model):
    idMateriel = models.AutoField(primary_key=True)
    nomMateriel = models.CharField(max_length=100)
    NumSerie = models.CharField(max_length=130)
    description = models.CharField(max_length=500)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.SET_DEFAULT, default=1)
    sous_categorie = models.ForeignKey(SousCategorie, on_delete=models.SET_DEFAULT, default=1)
    is_taken = models.BooleanField(default=False)
    en_panne = models.BooleanField(default=False)


class DemandeMateriel(models.Model):
    demandeur = models.ForeignKey(Employe, on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    date_debut = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=100 , default="pas encore traite")
    def __str__(self):
        return f"{self.demandeur} - {self.materiel} - {self.date_debut}"

    def get_demande_status_for_demandeur(self, demandeur_id):
        try:
            demande = DemandeMateriel.objects.get(materiel=self.materiel, demandeur_id=demandeur_id)
            return demande.status
        except DemandeMateriel.DoesNotExist:
            return None

class Demande_Materiel(models.Model):
    demandeur = models.ForeignKey(Employe, on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    date_demande = models.DateField()
    date_reponse = models.DateField()
    description = models.TextField()
    status = models.CharField(max_length=100 , default="pas encore traite")



