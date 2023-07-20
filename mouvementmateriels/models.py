from django.db import models

from employe.models import Employe
from materiels.models import Materiel

# Create your models here.

class MouvementMateriel(models.Model):
    idMouvement = models.AutoField(primary_key=True)
    dateMouvement = models.DateField()
    dateRetour = models.DateField(null=True, blank=True, default=None)
    description = models.CharField(max_length=200)
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    def _str_(self):
        return f"Mouvement ID: {self.id}, Date: {self.dateMouvement}, Employe: {self.employe.nom}, Materiel: {self.materiel.nomMateriel}"