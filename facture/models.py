from django.db import models

from fournisseur.models import Fournisseur

from django.core.validators import FileExtensionValidator

from materiels.models import Materiel

# Create your models here.

class Facture(models.Model):
    idFacture = models.AutoField(primary_key=True)
    #fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_facture = models.DateField()
    numero_facture = models.CharField(max_length=50, unique=True)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ville = models.CharField(max_length=30)
    #facture_pdf = models.FileField(upload_to='factures/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    facture_pdf = models.FileField(upload_to='factures/', null=True, blank=True)


class Article(models.Model):
    idArticle = models.AutoField(primary_key=True)
    materiel = models.ForeignKey(Materiel, null=True,on_delete=models.CASCADE)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)

class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    article = models.ForeignKey(Article,null=True, on_delete=models.CASCADE)
    #materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField(default=1)
    sous_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
