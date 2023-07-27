from django.db import models

from fournisseur.models import Fournisseur

# Create your models here.

class Facture(models.Model):
    idFacture = models.AutoField(primary_key=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_facture = models.DateField()
    numero_facture = models.CharField(max_length=50, unique=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ville = models.CharField(max_length=30)
    #facture_pdf = models.FileField(upload_to='factures/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    facture_pdf = models.FileField(upload_to='factures/', null=True, blank=True)
    

class Article(models.Model):
    idArticle = models.AutoField(primary_key=True)
    nom_article =  models.CharField(max_length=100)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    sous_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)