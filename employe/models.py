from django.db import models

class Employe(models.Model):
    idEmploye = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    dateEmbauche = models.CharField(max_length=100)
    email = models.CharField(max_length=130)