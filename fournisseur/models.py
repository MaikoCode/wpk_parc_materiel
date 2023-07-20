from django.db import models

class Fournisseur(models.Model):
    idFournisseur = models.AutoField(primary_key=True)
    nomFournisseur = models.CharField(max_length=200)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nomFournisseur
    
